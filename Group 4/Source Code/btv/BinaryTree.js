/**
 * @class Binary tree implementation.
 * 
 * @public
 * @constructor
 * @param {String} name The name of the tree
 */
btv.BinaryTree = function(name) {
    
    /**
     * The name of the tree.
     * 
     * @private
     * @type {String}
     */           
    this.name = "tree"; // default name
    this.setName(name); // if parameter name is given
    
    /**
     * The root node of the tree.
     * 
     * @private
     * @type {btv.BinaryTreeNode}
     */   
    this.root = null;
}

/**
 * @public
 * @param {String} name
 */
btv.BinaryTree.prototype.setName = function(name) {
    if(name != null) {
        this.name = name.toString();
    }
}

/**
 * @public
 * @returns {String}
 */
btv.BinaryTree.prototype.getName = function() {
    return this.name;
}

/**
 * @public
 * @param {btv.BinaryTreeNode} root
 * @throws Throws exception if the given node has a parent.
 */
btv.BinaryTree.prototype.setRoot = function(root) {    
    // It is not necessary. Tree can mean subtree too, but static btv.BinaryTree.getIndex(btv.BinaryTreeNode) still count index from the root of whole tree.
    if(root !== null && !root.isRoot()) {
        throw new btv.BinaryTreeException("The given node has a parent. Cannot be the root of a tree!");
    }
    
    // unset old root
    if(this.getRoot() !== null) {
        this.getRoot().setParent(null);
    }

    this.root = root;
}

/**
 * @public
 * @returns {btv.BinaryTreeNode}
 */
btv.BinaryTree.prototype.getRoot = function() {
    return this.root;
}

/**
 * @public
 * @returns {Number}
 */
btv.BinaryTree.prototype.getCount = function() {
    return this.getCountRec(this.getRoot());
}

/**
 * @private
 * @param {btv.BinaryTreeNode} node
 * @returns {Number}
 */
btv.BinaryTree.prototype.getCountRec = function(node) {
    if(node == null) {
        return 0;
    }
    
    return 1 + this.getCountRec(node.getLeft()) + this.getCountRec(node.getRight()); 
}

/**
 * @public
 * @param {Number[]} array
 */
btv.BinaryTree.prototype.build = function(array) {
    if(array.length <= 0) {
        this.setRoot(null);
        return;
    }
    
    var node = (new btv.BinaryTreeNode(array[0]));
    this.setRoot(node);
    
    this.buildLeftRec(array, 1, node);
    this.buildRightRec(array, 2, node);
}

/**
 * @private
 * @param {Number[]} array
 * @param {Number} index
 * @param {btv.BinaryTreeNode} parent
 */
btv.BinaryTree.prototype.buildLeftRec = function(array, index, parent) {
    if(index > array.length - 1) {
        return;
    }
    
    var node = new btv.BinaryTreeNode(array[index]);
    parent.setLeft(node);
    
    this.buildLeftRec(array, index*2 + 1, node);
    this.buildRightRec(array, index*2 + 2, node);    
}

/**
 * @private
 * @param {Number[]} array
 * @param {Number} index
 * @param {btv.BinaryTreeNode} parent
 */
btv.BinaryTree.prototype.buildRightRec = function(array, index, parent) {
    if(index > array.length - 1) {
        return;
    }
    
    var node = new btv.BinaryTreeNode(array[index]);
    parent.setRight(node);
    
    this.buildLeftRec(array, index*2 + 1, node);
    this.buildRightRec(array, index*2 + 2, node);    
}

/**
 * @public
 * @param {btv.BinaryTreeNode} node1
 * @param {btv.BinaryTreeNode} node2
 * @returns {Boolean} Returns true if nodes was swapped succesfully.
 */
btv.BinaryTree.prototype.swapNodes = function(node1, node2) {
    if(node1 === node2 || node1 == null || node2 == null) {
        return false;
    }
    
    // siblings
    if(node1.getParent() === node2.getParent()) {
        var tmp;
        if(node1.getParent().getLeft() === node1) { // n1 is left child 
            tmp = node1;
            node2.getParent().setLeft(node2);
            node2.getParent().setRight(tmp);
        } else  { // n2 is left child
            tmp = node2;
            node1.getParent().setLeft(node1);
            node1.getParent().setRight(tmp);            
        }
        
        return true;
    }
    
    // child
    if(node1.getLeft() === node2 || node1.getRight() === node2) { // n1 is parent n2
        return this.swapParentChild(node1, node2);
    }
    
    if(node2.getLeft() === node1 || node2.getRight() === node1) { // n2 is parent n1
        return this.swapParentChild(node2, node1);
    }
    
    // descendant (but not a child)
    var parent = node1.getParent();
    while(parent != null) {
        if(parent === node2) { // n1 is descendant of n2
            return this.swapAncestorDescendant(node2, node1);
        }
        parent = parent.getParent();
    }
    
    parent = node2.getParent();
    while(parent != null) {
        if(parent === node1) { // n1 is descendant of n2
            return this.swapAncestorDescendant(node1, node2);
        }
        parent = parent.getParent();
    }
    
    // 2 subtrees => n1 nor n2 are root
    var node2Left = node2.getLeft();
    var node2Right = node2.getRight();
    
    // set node2's new children
    node2.setLeft(node1.getLeft());
    node2.setRight(node1.getRight());
    
    // set node1's new children
    node1.setLeft(node2Left);
    node1.setRight(node2Right);
    
    // now subtrees swapped
    // swap parents - n1 nor n2 are root
        
    var node1parent = node1.getParent();
    var node2parent = node2.getParent();
        
    if(node1parent.getLeft() === node1) {
        node1parent.setLeft(node2);
    } else {
        node1parent.setRight(node2);
    }
        
    if(node2parent.getLeft() === node2) {
        node2parent.setLeft(node1);
    } else {
        node2parent.setRight(node1);
    }
        
    return true;
}

/**
 * @private
 * @param {btv.BinaryTreeNode} parent
 * @param {btv.BinaryTreeNode} child
 * @returns {Boolean} Returns true. Doesn't chceck if given child is child of given parent.
 */
btv.BinaryTree.prototype.swapParentChild = function(parent, child) {
    
    var parentLeft = parent.getLeft();
    var parentRight = parent.getRight();
    
    // set parent's new child
    parent.setLeft(child.getLeft());
    parent.setRight(child.getRight());
        
    // set child's parent
    if(parent.isRoot()) {
        this.setRoot(child);
    } else {
        if(parent.getParent().getLeft() === parent) {
            parent.getParent().setLeft(child);
        } else {
            parent.getParent().setRight(child)
        }
    }
        
    // set child's children
    if(child === parentLeft) {
        child.setLeft(parent);
        child.setRight(parentRight);
    } else {
        child.setLeft(parentLeft);
        child.setRight(parent);
    }
    
    return true;
}

/**
 * @private
 * @param {btv.BinaryTreeNode} ancestor
 * @param {btv.BinaryTreeNode} descendant
 * @returns {Boolean} Returns true. Doesn't chceck if given child is child of given parent.
 */
btv.BinaryTree.prototype.swapAncestorDescendant = function(ancestor, descendant) {
    
    var ancestortLeft = ancestor.getLeft();
    var ancestorRight = ancestor.getRight();
    
    // set ancestor's new children
    ancestor.setLeft(descendant.getLeft());
    ancestor.setRight(descendant.getRight());
    
    
    var ancestorParent = ancestor.getParent();
    var descendantParent = descendant.getParent();
    var descendantIsLeftChild;
    
    if(descendantParent.getLeft() === descendant) { // descendantParent still refer to ancestor, used below
        descendantIsLeftChild = true;
    } else {
        descendantIsLeftChild = false;
    }    
    
    // set descendant's new children
    descendant.setLeft(ancestortLeft);
    descendant.setRight(ancestorRight);
    
    // now subtrees swapped
    // swap parents

    // descendant new parent
    if(ancestor.isRoot()) {
        if(descendantParent.getLeft() === descendant) {
            descendantParent.setLeft(null);
        } else {
            descendantParent.setRight(null);
        }
        this.setRoot(descendant);
    } else {
        if(ancestorParent.getLeft() === ancestor) { // ancestorParent still refer to ancestor
            ancestorParent.setLeft(descendant);
        } else {
            ancestorParent.setRight(descendant);
        }
    }
    
    // ancestor new parent
    if(descendantIsLeftChild) { // descendantParent do not refer to descendant, becouse descendant parent was set to ancestorParent
        descendantParent.setLeft(ancestor);
    } else {
        descendantParent.setRight(ancestor);
    }
}

/**
 * @public
 * @returns {btv.BinaryTreeNode[]}
 */
btv.BinaryTree.prototype.toInorderArray = function() {
    var array = new Array();
    
    if(this.root === null) {
        return null;
    }
    
    btv.BinaryTree.toInorderArrayRec(this.root, array);
    
    return array;
}

/**
 * @private
 * @param {btv.BinaryTreeNode} node
 * @param {Array} [array] Optional, if given push node to that array, otherwise create new array.
 * @returns {btv.BinaryTreeNode[]} Returns given or new array.
 */
btv.BinaryTree.toInorderArrayRec = function(node, array) {
    if(node === null) {
        return null;
    }
    
    if(array == null) { // null or undefined
        array = new Array
    }
    
    btv.BinaryTree.toInorderArrayRec(node.getLeft(), array);
    array.push(node);
    btv.BinaryTree.toInorderArrayRec(node.getRight(), array);
    
    return array;
}

/**
 * Simulate array implementation.
 *
 * @public
 * @returns {btv.BinaryTreeNode[]}
 */
btv.BinaryTree.prototype.toArray = function() {
    var array = new Array();

    if(this.getRoot() == null) {
        return array;
    }

    // pomoci getNode(index)
    var maxIndex = 0;
    var nullCount = 0;
    
    for(var i = 0; i <= maxIndex; i++) {
        array[i] = this.getNode(i);
        if(array[i] !== null) {
            maxIndex = 2*i + 2; // have to check left and right child
            nullCount = 0;
        } else {
            nullCount++;
        }
    }
    
    array.length -= nullCount; // trim nulls at the end
    return array;
}

/**
 * Simulate array implementation.
 *
 * @public
 * @param {Number} index
 * @throws Throws exception if this tree doesn't have root node.
 * @throws Throws exception if given index is negative.
 * @returns {btv.BinaryTreeNode}
 */
btv.BinaryTree.prototype.getNode = function(index) {
    if(this.getRoot() === null) {
        throw new btv.BinaryTreeException("This tree doesn't have a root node.");
    }
    if(index < 0) {
        throw new btv.BinaryTreeException("The index cannot be negative.");
    }
    
    var path = "";

    while(index != 0) {
        if(index % 2 == 1) { // odd => left child
            index = (index-1)/2;
            path += "L";
        }else { // even => left child
            index = (index-2)/2;
            path += "R";
        }
    }
    
    var node = this.getRoot();
    for(var i = path.length; i > 0; i--) { // backwards 
        if(path.charAt(i-1) == "L") {
            node = node.getLeft();
        } else {
            node = node.getRight();
        }
        if(node === null) {
            return null;
        }
    }
    return node;
}

/**
 * Simulate array implementation.
 * 
 * @public
 * @static
 * @param {btv.BinaryTreeNode} node
 * @throws Throws exception if given node is null.
 * @returns {Number} Index of given node.
 */
btv.BinaryTree.getIndex = function(node) {
    if(node === null) {
        throw new btv.BinaryTreeException("Given node is null.");
    }
    
    if(node.isRoot()) // root
        return 0;
    
    // recursion
    var parentIndex = node.getParent().getIndex(); 
    
    if(node.getParent().getLeft() === node) { // this is left child 
        return 2*parentIndex + 1;
    }
    else { // this is right child 
        return 2*parentIndex + 2;
    }
}

/**
 * @public
 * @override
 * @returns {String}
 */
btv.BinaryTree.prototype.toString = function() {
    return "[object btv.BinaryTree" +
    " <name: '" + this.getName() + "'" +
    " root: " + this.getRoot() + ">]";  
}



////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////



/**
 * @class Binary tree node implementation.
 * 
 * @public
 * @constructor   
 * @param {Number|String} value The value of the node
 */
btv.BinaryTreeNode = function(value) {
    
    /**
     * The value of this node.
     * 
     * @private
     * @type {Number|String}
     */     
    this.value = value;
    
    /**
     * The parent of this node.
     *
     * @private
     * @type {btv.BinaryTreeNode}
     */
    this.parent = null;
    
    /**
     * The left child of this node.
     *
     * @private
     * @type {btv.BinaryTreeNode}
     */
    this.left = null;
    
    /**
     * The right child of this node.
     *
     * @private
     * @type {btv.BinaryTreeNode}
     */
    this.right = null;
}

/**
 * @public
 * @returns {Number}
 */
btv.BinaryTreeNode.prototype.getValue = function() {
    return this.value;
}

/**
 * @public
 * @see static function btv.BinaryTree#getIndex
 * @returns {Number}
 */
btv.BinaryTreeNode.prototype.getIndex = function() {
    return btv.BinaryTree.getIndex(this);
}

/**
 * @public
 * @returns {Boolean}
 */
btv.BinaryTreeNode.prototype.isRoot = function() {
    if(this.getParent() === null) {
        return true;
    } else {
        return false;
    }
}

/**
 * @public
 * @returns {Boolean}
 */
btv.BinaryTreeNode.prototype.isLeaf = function() {
    if(this.getLeft() === null && this.getRight() === null) {
        return true;
    } else {
        return false;
    }
}

/**
 * For method setLeft(BinaryTreeNode) and setRight(BinaryTreeNode) only!
 * Unset old reference oldParent to thisNode and 
 * set new reference thisNode to newParent,
 * DO NOT set reference newParent to thisNode!
 * Use setLeft(BinaryTreeNode) or setRight(BinaryTreeNode).
 * 
 * @private
 * @see btv.BinaryTreeNode#setLeft
 * @see btv.BinaryTreeNode#setRight
 * @param {btv.BinaryTreeNode} parent
 */
btv.BinaryTreeNode.prototype.setParent = function(parent) {
    // unset old reference
    if(!this.isRoot()) { // has parent
        if(this.getParent().getLeft() === this) { // this is left child 
            this.getParent().left = null;
        }
        else {// this is right child 
            this.getParent().right = null;
        }
    }
    // set new reference
    this.parent = parent;
}

/**
 * @public
 * @returns {btv.BinaryTreeNode}
 */
btv.BinaryTreeNode.prototype.getParent = function() {
    return this.parent;
}


/**
 * Set left child and changes all needed references.
 * 
 * @public
 * @throws Throws an exception if this node is same as given node - try to set yourself as a child of yourself.
 * @param {btv.BinaryTreeNode} left
 */
btv.BinaryTreeNode.prototype.setLeft = function(left) {
    if(this === left) {
        throw new btv.BinaryTreeNodeException("A node cannot be a child of yourself.");
    }
    
    if(left !== null) {
        left.setParent(this);
    }
    
    if(this.getLeft() !== null) {
        this.getLeft().setParent(null);
    }
    
    this.left = left;
}

/**
 * @public
 * @returns {btv.BinaryTreeNode}
 */
btv.BinaryTreeNode.prototype.getLeft = function() {
    return this.left;
}

/**
 * Set right child and changes all needed references.
 *
 * @public
 * @throws Throws an exception if this node is same as given node - try to set yourself as a child of yourself.
 * @param {btv.BinaryTreeNode} right
 */
btv.BinaryTreeNode.prototype.setRight = function(right) {
    if(this === right) {
        throw new btv.BinaryTreeNodeException("A node cannot be a child of yourself.");
    }
    
    if(right !== null) {
        right.setParent(this);
    }
    
    if(this.getRight() !== null) {
        this.getRight().setParent(null);
    }
    
    this.right = right;
}

/**
 * @public
 * @returns {btv.BinaryTreeNode}
 */
btv.BinaryTreeNode.prototype.getRight = function() {
    return this.right;
}

/**
 * @public
 * @override
 * @returns {String}
 */
btv.BinaryTreeNode.prototype.toString = function() {
    return "[object btv.BinaryTreeNode <value: " + this.getValue() + ", index: " + this.getIndex() + ">]";
}

