#include <stddef.h>
#include "lists.h"
/**
 * palindrome - check if is palindrome with recursion
 * @left: point to the left node
 * @right: point to the right node
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **left, listint_t *right)
{
	int result;

	if (right != NULL)
	{
		result = palindrome(left, right->next);
		if (result != 0)
		{
			result = (right->n == (*left)->n);
			*left = (*left)->next;
			return (result);
		}
		return (0);

	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of linked list
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
