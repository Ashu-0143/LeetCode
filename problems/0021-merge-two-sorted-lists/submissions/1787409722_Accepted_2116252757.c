struct ListNode* append(struct ListNode* lst2, struct ListNode* lst1)

{
    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* newNode = malloc(sizeof(struct ListNode));
    struct ListNode* prev = malloc(sizeof(struct ListNode));
    head = prev = lst1;
    head = head->next;
    newNode->val = lst2->val;
    printf("%d", newNode->val);
    printf("\n%d", lst1->val);
    if (newNode->val < lst1->val) {
        newNode->next = lst1;
        lst1 = newNode;
        return lst1;
    }
    while (head != NULL) {
        printf("\n%d-%d-%d", prev->val, newNode->val, head->val);
        if ((prev->val <= newNode->val) && (newNode->val <= head->val)) {
            printf("Executed : %d<%d<%d\n", prev->val, newNode->val, head->val);
            newNode->next = head;
            prev->next = newNode;
            return lst1;
        }
        head = head->next;
        prev = prev->next;
    }
    if (newNode->val >= prev->val) {
        newNode->next = NULL;
        prev->next = newNode;
    }
    return lst1;
}
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* temp = malloc(sizeof(struct ListNode));
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;
    while (list2 != NULL) {
        list1 = append(list2, list1);
        list2 = list2->next;
        temp = list1;
        printf("\nprinting list1 ... \n");
        while (temp != NULL) {
            printf("%d _ ", temp->val);
            temp = temp->next;
        }
    }
    return list1;
}
