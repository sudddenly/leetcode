/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> res1 = new ArrayList<Integer>();
        ArrayList<Integer> res2 = new ArrayList<Integer>();
        res1 = seekLeaf(root1,res1);
        res2 = seekLeaf(root2,res2);
        if(res1.size()!=res2.size()) return false;
        for(int i=0; i<res1.size(); i++){
            if(res1.get(i)!=res2.get(i)) return false;
        }
        return true;
    }
    public ArrayList seekLeaf(TreeNode root,ArrayList res){
        if(root==null) return res;
        if(root.left==null && root.right==null){
            res.add(root.val);
            return res;
        }
        res = seekLeaf(root.left,res);
        res = seekLeaf(root.right,res);
        return res;
    }
}