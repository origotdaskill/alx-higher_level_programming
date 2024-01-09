#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL;
    listint_t *second_half_reversed = NULL, *temp = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        prev_slow = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)  // Odd number of nodes, skip the middle one
    {
        mid = slow;
        slow = slow->next;
    }

    // Reverse the second half
    second_half_reversed = reverse_list(slow);

    // Compare the first half with the reversed second half
    temp = *head;
    while (second_half_reversed != NULL)
    {
        if (temp->n != second_half_reversed->n)
        {
            // Restore the original list and return false
            prev_slow->next = mid;
            mid->next = reverse_list(second_half_reversed);
            return 0;
        }
        temp = temp->next;
        second_half_reversed = second_half_reversed->next;
    }

    // Restore the original list
    prev_slow->next = mid;
    mid->next = reverse_list(second_half_reversed);

    return 1;
}
