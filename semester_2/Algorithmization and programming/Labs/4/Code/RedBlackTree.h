#pragma once

#include <iostream>
#include <iomanip>
#include <ostream>

enum RBTColor {BLACK, RED};

template <class Key>
struct RBTNode {
    Key key;
    RBTColor color;
    RBTNode<Key>* left;
    RBTNode<Key>* right;
    RBTNode<Key>* parent;

    RBTNode(Key k, RBTColor c, RBTNode* p, RBTNode* l, RBTNode* r):
        key(k), color(c), parent(p), left(l), right(r) {}
};

template <class T>
class RBTree {
private:
    void leftRotate(RBTNode<T>*& root, RBTNode<T>* x);
    void rightRotate(RBTNode<T>*& root, RBTNode<T>* y);
    
    void insert(RBTNode<T>*& root, RBTNode<T>* node);
    void insertFixUp(RBTNode<T>*& root, RBTNode<T>* node);
    void destroy(RBTNode<T>*& node);

    void remove(RBTNode<T>*& root, RBTNode<T>* node);
    void removeFixUp(RBTNode<T>*& root, RBTNode<T>* node, RBTNode<T>* parent);

    RBTNode<T>* search(RBTNode<T>* node, T key) const;
    void print(RBTNode<T>* node) const;
    void preOrder(RBTNode<T>* tree) const;
    void inOrder(RBTNode<T>* tree) const;
    void postOrder(RBTNode<T>* tree) const;

    RBTNode<T>* root;

public:
    RBTree();
    ~RBTree();
    
    void insert(T key);
    void remove(T Key);

    RBTNode<T>* search(T key);

    void print();
    void preOrder();
    void inOrder();
    void postOrder();
};

template <class T>
RBTree<T>::RBTree(): root(nullptr) {
    root = nullptr;
}

template <class T>
RBTree<T>::~RBTree() {
    destroy(root);
}

template <class T>
void RBTree<T>::leftRotate(RBTNode<T>*& root, RBTNode<T>* x) {
    RBTNode<T>* y = x->right;
    x->right = y->left;

    if (y->left != nullptr) {
        y->left->parent = x;
    }

    y->parent = x->parent;
    
    if (x->parent == nullptr) {
        root = y;
    } else {
        if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
    }
    
    y->left = x;
    x->parent = y;
}

template <class T>
void RBTree<T>::rightRotate(RBTNode<T>*& root, RBTNode<T>* y) {
    RBTNode<T>*x = y->left;
    y->left = x->right;

    if (x->right != nullptr) {
        x->right->parent = y;
    }

    x->parent = y->parent;
    
    if (y->parent == nullptr) {
        root = x;
    } else {
        if (y == y->parent->right) {
            y->parent->right = x;
        } else {
            y->parent->left = x;
        }
    }
    
    x->right = y;
    y->parent = x;
}

template <class T>
void RBTree<T>::insert(T key) {
    RBTNode<T>* z = new RBTNode<T>(key, RED, nullptr, nullptr, nullptr);
    insert(root, z);
}

template <class T>
void RBTree<T>::insert(RBTNode<T>*& root, RBTNode<T>* node) {
    RBTNode<T>* x = root;
    RBTNode<T>* y = nullptr;

    while (x != nullptr) {
        y = x;
        if (node->key > x->key) {
            x = x->right;
        } else {
            x = x->left;
        }
    }

    node->parent = y;
    
    if (y != nullptr) {
        if (node->key > y->key) {
            y->right = node;
        } else {
            y->left = node;
        }
    } else {
        root = node;
    }
    
    node->color = RED;
    insertFixUp(root, node);
}

template <class T>
void RBTree<T>::insertFixUp(RBTNode<T>*& root, RBTNode<T>* node) {
    RBTNode<T>* parent;
    parent = node->parent;

    while (node != RBTree::root && parent->color == RED) {
        RBTNode<T>* gparent = parent->parent;

        if (gparent->left == parent) {
            RBTNode<T>* uncle = gparent->right;
            if (uncle != nullptr && uncle->color == RED) {
                parent->color = BLACK;
                uncle->color = BLACK;
                gparent->color = RED;
                node = gparent;
                parent = node->parent;
            } else {
                if (parent->right == node) {
                    leftRotate(root, parent);
                    swap(node, parent);
                }
                rightRotate(root, gparent);
                gparent->color = RED;
                parent->color = BLACK;
                break;
            }
        } else {
            RBTNode<T>* uncle = gparent->left;
            if (uncle != nullptr && uncle->color == RED) {
                gparent->color = RED;
                parent->color = BLACK;
                uncle->color = BLACK;
                node = gparent;
                parent = node->parent;
            } else {
                if (parent->left == node) {
                    rightRotate(root, parent);
                    swap(parent, node);
                }
                leftRotate(root, gparent);
                parent->color = BLACK;
                gparent->color = RED;
                break;
            }
        }
    }
    
    root->color = BLACK;
}

template <class T>
void RBTree<T>::destroy(RBTNode<T>*& node) {
    if (node == nullptr) {
        return;
    }
    destroy(node->left);
    destroy(node->right);
    delete node;
    node = nullptr;
}

template <class T>
void RBTree<T>::remove(T key) {
    RBTNode<T>* deletenode = search(root, key);
    if (deletenode != nullptr) {
        remove(root, deletenode);
    }
}

template <class T>
void RBTree<T>::remove(RBTNode<T>*& root, RBTNode<T>* node) {
    RBTNode<T>* child;
    RBTNode<T>* parent;

    RBTColor color;

    if (node->left != nullptr && node->right != nullptr) {
        RBTNode<T>* replace = node;
        replace = node->right;

        while (replace->left != nullptr) {
            replace = replace->left;
        }
        
        if (node->parent != nullptr) {
            if (node->parent->left == node) {
                node->parent->left = replace;
            } else {
                node->parent->right = replace;
            }
        } else {
            root = replace;
        }

        child = replace->right;
        parent = replace->parent;
        color = replace->color;

        if (parent == node) {
            parent = replace;
        } else {
            if (child != nullptr) {
                child->parent = parent;
            }
            parent->left = child;
            replace->right = node->right;
            node->right->parent = replace;
        }

        replace->parent = node->parent;
        replace->color = node->color;
        replace->left = node->left;
        node->left->parent = replace;

        if (color == BLACK) {
            removeFixUp(root, child, parent);
        }

        delete node;
        return;
    }

    if (node->left != nullptr) {
        child = node->left;
    } else {
        child = node->right;
    }

    parent = node->parent;
    color = node->color;

    if (child) {
        child->parent = parent;
    }
    
    if (parent) {
        if (node == parent->left) {
            parent->left = parent;
        } else {
            parent->right = child;
        }
    } else {
        RBTree::root = child;
    }

    if (color == BLACK) {
        removeFixUp(root, child, parent);
    }

    delete node;
}

template <class T>
void RBTree<T>::removeFixUp(RBTNode<T>*& root, RBTNode<T>* node, RBTNode<T>* parent) {
    RBTNode<T>* othernode;

    while ((!node) || node->color == BLACK && node != RBTree::root) {
        if (parent->left == node) {
            othernode = parent->right;
            if (othernode->color == RED) {
                othernode->color = BLACK;
                parent->color = RED;
                leftRotate(root, parent);
                othernode = parent->right;
            } else {
                if (!(othernode->right) || othernode->right->color == BLACK) {
                    othernode->left->color = BLACK;
                    othernode->color = RED;
                    rightRotate(root, othernode);
                    othernode = parent->right;
                }
                othernode->color = parent->color;
                parent->color = BLACK;
                othernode->right->color = BLACK;
                leftRotate(root, parent);
                node = root;
                break;
            }
        } else {
            othernode = parent->left;

            if (othernode->color == RED) {
                othernode->color = BLACK;
                parent->color = RED;
                rightRotate(root, parent);
                othernode = parent->left;
            }

            if ((!othernode->left || othernode->left->color == BLACK) && (!othernode->right || othernode->right->color == BLACK)) {
                othernode->color = RED;
                node = parent;
                parent = node->parent;
            } else {
                if (!(othernode->left) || othernode->left->color == BLACK) {
                    othernode->right->color = BLACK;
                    othernode->color = RED;
                    leftRotate(root, othernode);
                    othernode = parent->left;
                }

                othernode->color = parent->color;
                parent->color = BLACK;
                othernode->left->color = BLACK;
                rightRotate(root, parent);
                node = root;
                break;
            }
        }
    }

    if (node) {
        node->color = BLACK;
    }
}

template <class T>
RBTNode<T>* RBTree<T>::search(T key) {
    return search(root, key);
}

template <class T>
RBTNode<T>* RBTree<T>::search(RBTNode<T>* node, T key) const {
    if (node == nullptr || node->key == key) {
        return node;
    } else {
        if (key > node->key) {
            return search(node->right, key);
        } else {
            return search(node->left, key);
        }
    }
}

template <class T>
void RBTree<T>::print() {
    if (root == nullptr) {
        std::cout << "[-] Empty RBTree" << std::endl;
    } else {
        print(root);
    }
}

template <class T>
void RBTree<T>::print(RBTNode<T>* node) const {
    if (node == nullptr) {
        return;
    }

    if (node->parent == nullptr) {
        std::cout << "[+] " << node->key << "(" << node->color << ") is root" << std::endl;
    } else if (node->parent->left == node) {
        std::cout << "[+] " << node->key << "(" << node->color << ") is " << node->parent->key << " left children" << std::endl;
    } else {
        std::cout << "[+] " << node->key << "(" << node->color << ") is " << node->parent->key << " right children" << std::endl;
    }

    print(node->left);
    print(node->right);
}

template <class T>
void RBTree<T>::preOrder() {
    if (root == nullptr) {
        std::cout << "[-] Empty" << std::endl;
    } else {
        preOrder(root);
    }
}

template <class T>
void RBTree<T>::preOrder(RBTNode<T>* tree) const {
    if (tree != nullptr) {
        std::cout << tree->key << " ";
        preOrder(tree->left);
        preOrder(tree->right);
    }
}

template <class T>
void RBTree<T>::inOrder() {
    if (root == nullptr) {
        std::cout << "[-] Empty" << std::endl;
    } else {
        inOrder(root);
    }
}

template <class T>
void RBTree<T>::inOrder(RBTNode<T>* tree) const {
    if (tree != nullptr) {
        inOrder(tree->left);
        std::cout << tree->key << " ";
        inOrder(tree->right);
    }
}

template <class T>
void RBTree<T>::postOrder() {
    if (root == nullptr) {
        std::cout << "[-] Empty" << std::endl;
    } else {
        postOrder(root);
    }
}

template <class T>
void RBTree<T>::postOrder(RBTNode<T>* tree) const {
    if (tree != nullptr) {
        postOrder(tree->left);
        postOrder(tree->right);
        std::cout << tree->key << " ";
    }
}

