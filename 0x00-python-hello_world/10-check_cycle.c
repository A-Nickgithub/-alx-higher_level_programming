#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: pointer that contains the next address of the node
 *
 * Return: 1 if the linked list is circular and 0 if it is not
 */
int check_cycle(listint_t *list)
{
	int n = 0;

	if (!list)
	{
		return (0);
	}
	while (list)
	{
		list = list->next;
		n++;
		if (n > 100)
		{
			return (1);
		}
	}
	return (0);
}

