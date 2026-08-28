bool hasCycle(struct ListNode *head) {
    struct ListNode *slow=head;
    struct ListNode *fast=head;
    while(slow!=NULL)
    {
        if (fast->next==NULL||fast->next->next==NULL)
        return 0;
        if (slow=head)
        slow=slow->next;        
        if(slow==fast)
        break;
        slow=slow->next;
        fast=fast->next->next;
    }
    return 1;
}
