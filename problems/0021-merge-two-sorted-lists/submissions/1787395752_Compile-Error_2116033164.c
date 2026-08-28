struct ListNode* append(int val, struct ListNode* lst1)

{
    struct ListNode* head;
    struct ListNode* newNode;
    struct ListNode* prev;
    struct ListNode* temp;
   
    head = head->next;
    if (val <= min) {
        newNode->val = val;
        newNode->next = lst1;
        lst1 = newNode;
        return lst1;
    }
    while (head != NULL) {   
        if ((prev->val <= val) || (head->val >= val)) {
            newNode->next = head;
            prev->next = newNode;
            lst1 = prev;
            return lst1;
        }
        head = head->next;
        prev = prev->next;
    }
    max = prev->val;
    return lst1;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* temp;
    temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    while (list2 != NULL) {
        append(list2->val, list1);
        list2 = list2->next;
    }
    return list1;
}
