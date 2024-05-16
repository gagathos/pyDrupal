def generate_create_node_type_code(name, label):
    """
    Generates PHP code to create a new Drupal node type (content type).

    Args:
        name (str): The machine name of the node type.
        label (str): The human-readable label of the node type.

    Returns:
        str: The generated PHP code.
    """
    
    php_code = f"""
    use Drupal\\node\\Entity\\NodeType;

    // Create node type
    $node_type = NodeType::create([
        'type' => '{name}',
        'name' => '{label}'
    ]);
    $node_type->save();
    """
    
    return php_code
