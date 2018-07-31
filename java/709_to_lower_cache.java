class Solution {
    public String toLowerCase(String str) {
       char[] ss = str.toCharArray();
        for(int i=0;i<ss.length;i++){
            if(ss[i]>='A'&&ss[i]<='Z'){
                ss[i]+=32;
            }
        }
        return new String(ss);
    }
}