def generate_add_field_code(entity_type, bundle, field):
    """
    Generates PHP code to add a single field to an existing Drupal entity type.

    Args:
        entity_type (str): The machine name of the entity type (e.g., 'node').
        bundle (str): The machine name of the bundle (content type) to which the field will be added.
        field (dict): A dictionary representing the field to be added.
            The dictionary should contain:
                - name (str): The machine name of the field.
                - type (str): The field type (e.g., 'string', 'integer', 'text', 'text_long', 'text_with_summary').
                - label (str): The human-readable label of the field.
                - cardinality (int, optional): The number of values allowed for the field. Defaults to 1.
                - required (bool, optional): Whether the field is required. Defaults to False.
                - default_value (any, optional): The default value for the field. Defaults to None.
                - description (str, optional): A description for the field. Defaults to an empty string.

    Returns:
        str: The generated PHP code.
    """
    
    php_code = f"""
    use Drupal\\field\\Entity\\FieldStorageConfig;
    use Drupal\\field\\Entity\\FieldConfig;

    // Add field storage
    $field_storage = FieldStorageConfig::create([
        'field_name' => '{field['name']}',
        'entity_type' => '{entity_type}',
        'type' => '{field['type']}',
        'cardinality' => {field.get('cardinality', 1)},
    ]);
    $field_storage->save();

    // Add field instance
    $field_instance = FieldConfig::create([
        'field_storage' => $field_storage,
        'bundle' => '{bundle}',
        'label' => '{field['label']}',
        'required' => {str(field.get('required', False)).lower()},
        'description' => '{field.get('description', '')}',
    ]);
    $field_instance->save();
    """
    if 'default_value' in field:
        php_code += f"""
        $field_instance->setDefaultValue({repr(field['default_value'])});
        $field_instance->save();
        """
    
    return php_code
