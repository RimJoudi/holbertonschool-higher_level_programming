#include "lists.h"
/**
*check_cycle - checks if a singly linked list has a cycle in it.
*@list: listint_t
*Return: 0 for no cycle, otherwise 1.
*/
int check_cycle(listint_t *list)
{
listint_t *head;
listint_t *tmp;
tmp = list;
head = list->next;
if (list == NULL)
return (0);
while (tmp != NULL && head != NULL && head->next)
{
if (tmp == head)
return (1);
tmp = tmp->next;
head = head->next->next;
}
return (0);
}
