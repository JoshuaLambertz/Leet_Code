class Solution {

    public int lengthAfterTransformations(String s, int t) {
        StringBuilder sNew = new StringBuilder(s);

        for (int step = 0; step < t; step++) {
            StringBuilder next = new StringBuilder();
            
            for (int i = 0; i < sNew.length(); i++) {
                //Char = ASCII Tabelle :)
                char str = sNew.charAt(i);
                
                if (str == 'z') {
                    next.append("ab");
                } else {
                    next.append((char)(str + 1));
                }
            }

            sNew = next;
        }

        return sNew.length();
    }
}