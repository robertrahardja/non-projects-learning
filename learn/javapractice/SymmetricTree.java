//Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Treenode {
  int val;
  Treenode left;
  Treenode right;

  Treenode(int val) {
    this.val = val;
  }
}

public class SymmetricTree {

  public static void main(String[] args) {
    Treenode root = new Treenode(1);

    root.left = new Treenode(2);
    root.right = new Treenode(2);
    root.left.left = new Treenode(3);
    root.left.right = new Treenode(4);
    root.right.left = new Treenode(4);
    root.right.right = new Treenode(3);

    Queue<Treenode> queue = new LinkedList<>();

    queue.add(root);

    while (!queue.isEmpty()) {
      Treenode node = queue.poll();

      System.out.println(node.val + " ");

      if (node.left != null) {
        queue.add(node.left);
      }

      if (node.left != null) {
        queue.add(node.right);
      }

    }

  }
}
