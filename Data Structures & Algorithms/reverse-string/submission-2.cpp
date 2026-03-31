class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int lenght = size(s);
        while(i < lenght / 2)
        {
            int tmp = s[i];
            s[i] = s[lenght - i - 1];
            s[lenght - i - 1] = tmp;
            i++;
        }
    }
};