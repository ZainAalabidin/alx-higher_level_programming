#include "lists.h"

/**
 * check_cycle - check if list has cycle
 * @list: linked list
 * Return: 1 if cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	if (list)
		return (0);
	while (x && y && y->next)
	{
		x = x->next;
		y = y->next->next;
		if (y == x)
			return (1);
	}
	return (0);
}
