#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *prev_slow, *mid, *second_half_copy, *second_half_reversed;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    slow = fast = *head;
    prev_slow = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    second_half_copy = copy_list(slow);

    second_half_reversed = reverse_list(second_half_copy);
    prev_slow->next = NULL;

    palindrome = compare_lists(*head, second_half_reversed);

    free_listint(second_half_reversed);

    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = second_half_copy;
    }
    else
    {
        prev_slow->next = second_half_copy;
    }

    return palindrome;
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

