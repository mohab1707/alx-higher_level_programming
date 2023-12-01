#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);
listint_t *slow = *head, *fast = *head;
listint_t *prev_slow = NULL, *mid = NULL;
int result = 1;
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
listint_t *second_half = reverse_list(&slow);
result = compare_lists(*head, second_half);
if (mid != NULL)
{
prev_slow->next = mid;
mid->next = second_half;
}
else
{
prev_slow->next = second_half;
}
return (result);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
return (*head);
}

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
while (list1 != NULL && list2 != NULL)
{
if (list1->n == list2->n)
{
list1 = list1->next;
list2 = list2->next;
}
else
{
return (0);
}
}
return (list1 == NULL && list2 == NULL);
}
