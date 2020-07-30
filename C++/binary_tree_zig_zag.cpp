/*
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
time: O(V + E)
space: O(H)
Author: Will Cray
Date: 1/9/2020
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root)
    {
        // solution 1: BFS with modified order based on bool value
        // time - O(V + E), space - O(H)

        // check for null input
        if (root == NULL)
        {
            return {};
        }

        // init return vector
        vector<vector<int>> traversal;

        // init queue
        queue<TreeNode*> q;

        // add root to queue
        q.push(root);

        // BFS
        bool leftToRight = true;

        while (! q.empty())
        {
            int size = q.size();
            vector<int> layer = vector<int>(size);

            for (int i = 0; i < size; ++i)
            {
                TreeNode *node = q.front();
                q.pop();

                int index = i;
                if (!leftToRight)
                {
                    index = size - i - 1;
                }

                layer.at(index) = node->val;

                // add children to queue if they're not null

                if (node->left)
                {
                    q.push(node->left);
                }

                if (node->right)
                {
                    q.push(node->right);
                }
            }

            // after each layer
            traversal.push_back(layer);
            leftToRight = !leftToRight;
        }
        return traversal;
    }
};
