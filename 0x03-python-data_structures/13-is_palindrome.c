#include "lists.h"

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *curr = head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return (prev);
}


int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	listint_t *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast == NULL)
		slow = slow->next;

	second_half = reverse_list(slow);
	temp = *head;

	while (second_half != NULL)
	{
		if (temp->n != second_half->n)
			return (0);
		temp = temp->next;
		second_half = second_half->next;
	}

	return (1);
}
