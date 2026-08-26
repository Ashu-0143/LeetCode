bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies,
                      int* returnSize) {

    bool* lst = malloc(candiesSize * sizeof(bool));
    int high = 0, temp;
    for (int j = 0; j < candiesSize; j++) {
        if (candies[j] > high)
            high = candies[j];
    }
    for (int i = 0; i < candiesSize; i++) {
        temp = candies[i] + extraCandies;
        if (temp >= high)

            lst[i] = true;
        else

            lst[i] = false;
    }
    *returnSize = candiesSize;
    return lst;
}
