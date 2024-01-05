#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check whether is palidrome or not
 * @head: pointer to the pointer if the head
 * Return: 1 if palindrome or 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int tmp[100], a = 0, b = 0;

	if (!*head || !head || !current->next)
	{
		return (1);
	}
	while (current)
	{
		tmp[a] = current->n;
		a++;
		current = current->next;
	}
	a--;
	while (b <= a)
	{
		if (tmp[b] != tmp[a])
		{
			return (0);
		}
		b++;
		a--;
	}
	return (1);
}
