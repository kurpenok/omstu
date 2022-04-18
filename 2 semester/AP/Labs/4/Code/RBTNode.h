enum RBTColor {BLACK, KEY};

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

