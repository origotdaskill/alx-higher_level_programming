#include "lists.h"

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
/**
 * copy_list - creates a copy of a linked list
 * @head: pointer to the head of the original list
 * Return: pointer to the head of the copied list
 */
listint_t *copy_list(listint_t *head)
{
    listint_t *new_head = NULL;
    listint_t *current = head;

    while (current != NULL)
    {
        add_nodeint_end(&new_head, current->n);
        current = current->next;
    }

    return new_head;
}

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
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;

        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}

