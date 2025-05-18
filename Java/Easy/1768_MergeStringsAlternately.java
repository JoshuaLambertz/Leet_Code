/* You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: 
        The merged string will be merged as so:
        word1:  a   b   c
        word2:    p   q   r
        merged: a p b q c r

Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation:
        Notice that as word2 is longer, "rs" is appended to the end.
        word1:  a   b 
        word2:    p   q   r   s
        merged: a p b q   r   s

Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation:
        Notice that as word1 is longer, "cd" is appended to the end.
        word1:  a   b   c   d
        word2:    p   q 
        merged: a p b q c   d */

//My Solution
class Solution {
    public String mergeAlternately(String word1, String word2) {
        
        ArrayList<Character> arr = new ArrayList<>();
        for (char x : word1.toCharArray()) {
            arr.add(x);
        }

        int insertPos = 1;

        for (int i = 0; i < word2.length(); i++) {
            char letter = word2.charAt(i);

            if (insertPos > arr.size()) {
                arr.add(letter);
            } else {
                arr.add(insertPos, letter);
            }
            insertPos += 2;
        }

        StringBuilder sb = new StringBuilder();
        for (char x : arr) {
            sb.append(x);
        }
        return sb.toString();
    }
}

//Best Practise
class Solution {
    public String mergeAlternately(String word1, String word2) {

        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        int str1 = word1.length(), str2 = word2.length();
        
        while(i < str1 || j < str2){
           if(i < str1) sb.append(word1.charAt(i++));
           if(j < str2) sb.append(word2.charAt(j++));
        }
        return sb.toString();
    }
}