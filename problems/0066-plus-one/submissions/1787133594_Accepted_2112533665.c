int* valueChanger(int* pointer, int size, int* returnSize) {
    if (size == 0) {
        int new_size = *returnSize + 1;
        int* temp = (int*)realloc(pointer, new_size * sizeof(int));
        pointer = temp;
        for (int i = new_size - 1; i > 0; i--) {
            pointer[i] = pointer[i - 1];
        }
        pointer[0] = 1;
        *returnSize = new_size;
        return pointer;
    }
    if (pointer[size - 1] == 9) {
        pointer[size - 1] = 0;
        return valueChanger(pointer, size - 1, returnSize);
    } else {
        pointer[size - 1]++;
        return pointer;
    }
}

int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* digitss = (int*)malloc(digitsSize * sizeof(int));
    for (int i = 0; i < digitsSize; i++) {
        digitss[i] = digits[i];
    }
    
    *returnSize = digitsSize;
    int size = digitsSize;
    int* result = valueChanger(digitss, size, returnSize);
    return result;
}
