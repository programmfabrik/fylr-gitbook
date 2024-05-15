---

---

# Sample Datamodel

This is an overview over the datamodel that is used as a basis for the tutorial on the JSON Importer.

## Tables

### Linked Objects (not searchable objects)

* **Orte** (`orte`)
	* is hierarchical
	* Field `name` has a unique constraint and will be used as the reference

* **Personen** (`personen`)
	* Field `name` has a unique constraint and will be used as the reference

* **Schlagwörter** (`schlagwoerter`)
	* Field `inventarnummer` has a unique constraint and will be used as the reference

### Main Objects (searchable objects)

* **Objekte** (`objekte`)
	* has pool management
	* contains a reverse editable link to **Bilder** (*1 to N* relation between `objekte` and `bilder`)
	* Field `inventarnummer` has a unique constraint and will be used as the reference

* **Bilder** (`bilder`)
	* has pool management
	* has an asset field (`datei`)
	* contains a link to **Orte** (`aufnahmeort`)
	* contains links to **Personen** (`person`) in a nested table (`personen`)
	* contains links to **Schlagwörter** (`schlagwort`) in a nested table (`schlagwoerter`)
	* contains a reverse link to **Objekte** (*N to 1* relation between `bilder` and `objekte`)
	* Field `reference` was added as a hidden, unique field to be used as the reference

## Datamodel to download

```json
{
    "version": 1,
    "format_version": 1,
    "schema": {
        "based_on_base_version": 230,
        "l10n_languages": [],
        "max_column_id": 18,
        "max_table_id": 8,
        "tables": [
            {
                "acl_table": false,
                "columns": [
                    {
                        "column_id": 1,
                        "kind": "column",
                        "name": "name",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_oneline"
                    },
                    {
                        "column_id": 2,
                        "kind": "column",
                        "name": "adresse",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text"
                    }
                ],
                "foreign_keys": [],
                "has_tags": false,
                "in_main_search": false,
                "is_hierarchical": false,
                "name": "personen",
                "pool_link": false,
                "table_id": 1,
                "unique_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 1,
                                "column_name_hint": "name"
                            }
                        ],
                        "name": "personen__name_unique"
                    }
                ]
            },
            {
                "acl_table": false,
                "columns": [
                    {
                        "column_id": 3,
                        "kind": "column",
                        "name": "name",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_oneline"
                    }
                ],
                "foreign_keys": [],
                "has_tags": false,
                "in_main_search": false,
                "is_hierarchical": true,
                "name": "orte",
                "pool_link": false,
                "table_id": 2,
                "unique_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 3,
                                "column_name_hint": "name"
                            }
                        ],
                        "name": "orte__name_unique"
                    }
                ]
            },
            {
                "acl_table": false,
                "columns": [
                    {
                        "column_id": 4,
                        "kind": "column",
                        "name": "name",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_oneline"
                    }
                ],
                "foreign_keys": [],
                "has_tags": false,
                "in_main_search": false,
                "is_hierarchical": false,
                "name": "schlagwoerter",
                "pool_link": false,
                "table_id": 3,
                "unique_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 4,
                                "column_name_hint": "name"
                            }
                        ],
                        "name": "schlagwoerter__name_unique"
                    }
                ]
            },
            {
                "acl_table": false,
                "columns": [
                    {
                        "column_id": 5,
                        "kind": "column",
                        "name": "datei",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "eas"
                    },
                    {
                        "column_id": 6,
                        "kind": "column",
                        "name": "titel",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_l10n"
                    },
                    {
                        "column_id": 7,
                        "kind": "column",
                        "name": "beschreibung",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text"
                    },
                    {
                        "column_id": 8,
                        "kind": "column",
                        "name": "aufnahmedatum",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "date"
                    },
                    {
                        "column_id": 9,
                        "kind": "column",
                        "name": "aufnahmeort",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "link"
                    },
                    {
                        "kind": "link",
                        "not_null": false,
                        "other_table_id": 5,
                        "other_table_name_hint": "bilder__personen"
                    },
                    {
                        "kind": "link",
                        "not_null": false,
                        "other_table_id": 6,
                        "other_table_name_hint": "bilder__schlagwoerter"
                    },
                    {
                        "column_id": 17,
                        "kind": "column",
                        "name": "objekte",
                        "not_null": false,
                        "reverse_edit": true,
                        "type": "link"
                    },
                    {
                        "column_id": 18,
                        "kind": "column",
                        "name": "reference",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "string"
                    }
                ],
                "foreign_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 9,
                                "column_name_hint": "aufnahmeort"
                            }
                        ],
                        "name": "bilder__aufnahmeort__orte_fkey",
                        "on_delete": "restrict",
                        "on_update": "cascade",
                        "referenced_table": {
                            "columns": [
                                {
                                    "auto_column_primary_key": true
                                }
                            ],
                            "name_hint": "orte",
                            "table_id": 2
                        }
                    },
                    {
                        "columns": [
                            {
                                "column_id": 17,
                                "column_name_hint": "objekte"
                            }
                        ],
                        "name": "bilder__objekte__objekte_fkey",
                        "on_delete": "cascade",
                        "on_update": "cascade",
                        "referenced_table": {
                            "columns": [
                                {
                                    "auto_column_primary_key": true
                                }
                            ],
                            "name_hint": "objekte",
                            "table_id": 8
                        }
                    }
                ],
                "has_tags": false,
                "in_main_search": true,
                "is_hierarchical": false,
                "name": "bilder",
                "pool_link": true,
                "table_id": 4,
                "unique_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 18,
                                "column_name_hint": "reference"
                            }
                        ],
                        "name": "bilder__reference_unique"
                    }
                ]
            },
            {
                "columns": [
                    {
                        "column_id": 10,
                        "kind": "column",
                        "name": "person",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "link"
                    },
                    {
                        "column_id": 11,
                        "kind": "column",
                        "name": "bemerkung",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_oneline"
                    }
                ],
                "foreign_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 10,
                                "column_name_hint": "person"
                            }
                        ],
                        "name": "bilder__personen__person__personen_fkey",
                        "on_delete": "restrict",
                        "on_update": "cascade",
                        "referenced_table": {
                            "columns": [
                                {
                                    "auto_column_primary_key": true
                                }
                            ],
                            "name_hint": "personen",
                            "table_id": 1
                        }
                    }
                ],
                "name": "bilder__personen",
                "owned_by": {
                    "other_table_id": 4,
                    "other_table_name_hint": "bilder"
                },
                "table_id": 5,
                "unique_keys": []
            },
            {
                "columns": [
                    {
                        "column_id": 12,
                        "kind": "column",
                        "name": "schlagwort",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "link"
                    }
                ],
                "foreign_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 12,
                                "column_name_hint": "schlagwort"
                            }
                        ],
                        "name": "bilder__schlagwoerter__schlagwort__schlagwoerter_fkey",
                        "on_delete": "restrict",
                        "on_update": "cascade",
                        "referenced_table": {
                            "columns": [
                                {
                                    "auto_column_primary_key": true
                                }
                            ],
                            "name_hint": "schlagwoerter",
                            "table_id": 3
                        }
                    }
                ],
                "name": "bilder__schlagwoerter",
                "owned_by": {
                    "other_table_id": 4,
                    "other_table_name_hint": "bilder"
                },
                "table_id": 6,
                "unique_keys": []
            },
            {
                "acl_table": false,
                "columns": [
                    {
                        "column_id": 15,
                        "kind": "column",
                        "name": "inventarnummer",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "text_oneline"
                    },
                    {
                        "column_id": 16,
                        "kind": "column",
                        "name": "datierung",
                        "not_null": false,
                        "reverse_edit": false,
                        "type": "daterange"
                    },
                    {
                        "kind": "reverse_link",
                        "not_null": false,
                        "other_column_id": 17,
                        "other_column_name_hint": "objekte",
                        "other_table_id": 4,
                        "other_table_name_hint": "bilder"
                    }
                ],
                "foreign_keys": [],
                "has_tags": true,
                "in_main_search": true,
                "is_hierarchical": false,
                "name": "objekte",
                "pool_link": true,
                "table_id": 8,
                "unique_keys": [
                    {
                        "columns": [
                            {
                                "column_id": 15,
                                "column_name_hint": "inventarnummer"
                            }
                        ],
                        "name": "objekte__inventarnummer_unique"
                    }
                ]
            }
        ],
        "type": "user",
        "version": 1
    },
    "mask": {
        "based_on_schema_version": 1,
        "masks": [
            {
                "comment": "",
                "fields": [
                    {
                        "column_id": 1,
                        "column_name_hint": "name",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma",
                                "order": 1
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 2,
                        "column_name_hint": "adresse",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    }
                ],
                "hide_in_detail": false,
                "hide_in_editor": false,
                "hide_in_print_dialog": false,
                "is_preferred": true,
                "mask_id": 1,
                "name": "personen__all_fields",
                "require_comment": "never",
                "system_fields": {
                    "acl": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "collections": {
                        "edit": {
                            "mode": "show"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "object_id": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "owner": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "parent": {
                        "edit": {
                            "mode": "off"
                        },
                        "inline": "standard",
                        "mask_id": "PREFERRED",
                        "output": {
                            "mode": "off"
                        }
                    },
                    "pool": {
                        "output": {
                            "mode": "show"
                        }
                    },
                    "publish": {
                        "output": {
                            "mode": "off"
                        }
                    },
                    "tags": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    }
                },
                "table_id": 1,
                "table_name_hint": "personen"
            },
            {
                "comment": "",
                "fields": [
                    {
                        "column_id": 3,
                        "column_name_hint": "name",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma",
                                "order": 1
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    }
                ],
                "hide_in_detail": false,
                "hide_in_editor": false,
                "hide_in_print_dialog": false,
                "is_preferred": true,
                "mask_id": 2,
                "name": "orte__all_fields",
                "require_comment": "never",
                "system_fields": {
                    "acl": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "collections": {
                        "edit": {
                            "mode": "show"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "object_id": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "owner": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "parent": {
                        "edit": {
                            "mode": "edit"
                        },
                        "inline": "standard",
                        "mask_id": "SAME",
                        "output": {
                            "mode": "show"
                        }
                    },
                    "pool": {
                        "output": {
                            "mode": "show"
                        }
                    },
                    "publish": {
                        "output": {
                            "mode": "off"
                        }
                    },
                    "tags": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    }
                },
                "table_id": 2,
                "table_name_hint": "orte"
            },
            {
                "comment": "",
                "fields": [
                    {
                        "column_id": 4,
                        "column_name_hint": "name",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma",
                                "order": 1
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    }
                ],
                "hide_in_detail": false,
                "hide_in_editor": false,
                "hide_in_print_dialog": false,
                "is_preferred": true,
                "mask_id": 3,
                "name": "schlagworte__all_fields",
                "require_comment": "never",
                "system_fields": {
                    "acl": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "collections": {
                        "edit": {
                            "mode": "show"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "object_id": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "owner": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "parent": {
                        "edit": {
                            "mode": "off"
                        },
                        "inline": "standard",
                        "mask_id": "PREFERRED",
                        "output": {
                            "mode": "off"
                        }
                    },
                    "pool": {
                        "output": {
                            "mode": "show"
                        }
                    },
                    "publish": {
                        "output": {
                            "mode": "off"
                        }
                    },
                    "tags": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    }
                },
                "table_id": 3,
                "table_name_hint": "schlagwoerter"
            },
            {
                "comment": "",
                "fields": [
                    {
                        "column_id": 5,
                        "column_name_hint": "datei",
                        "custom_settings": {
                            "show_in_map": true
                        },
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {
                                "order": 1
                            },
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 6,
                        "column_name_hint": "titel",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma",
                                "order": 1
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 7,
                        "column_name_hint": "beschreibung",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 8,
                        "column_name_hint": "aufnahmedatum",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 9,
                        "column_name_hint": "aufnahmeort",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "inline": "standard",
                        "kind": "link",
                        "mask_id": "PREFERRED",
                        "other_table_id": 2,
                        "other_table_name_hint": "orte",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "custom_settings": {},
                        "edit": {
                            "append_only": false,
                            "as_table": false,
                            "mode": "edit",
                            "show_labels": false
                        },
                        "kind": "linked-table",
                        "mask": {
                            "comment": "",
                            "fields": [
                                {
                                    "column_id": 10,
                                    "column_name_hint": "person",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "inline": "standard",
                                    "kind": "link",
                                    "mask_id": "PREFERRED",
                                    "other_table_id": 1,
                                    "other_table_name_hint": "personen",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 11,
                                    "column_name_hint": "bemerkung",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                }
                            ],
                            "hide_in_detail": false,
                            "hide_in_editor": false,
                            "hide_in_print_dialog": false,
                            "is_preferred": false,
                            "table_id": 5,
                            "table_name_hint": "bilder__personen"
                        },
                        "other_table_id": 5,
                        "other_table_name_hint": "bilder__personen",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "custom_settings": {},
                        "edit": {
                            "append_only": false,
                            "as_table": false,
                            "mode": "edit",
                            "show_labels": false
                        },
                        "kind": "linked-table",
                        "mask": {
                            "comment": "",
                            "fields": [
                                {
                                    "column_id": 12,
                                    "column_name_hint": "schlagwort",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "inline": "standard",
                                    "kind": "link",
                                    "mask_id": "PREFERRED",
                                    "other_table_id": 3,
                                    "other_table_name_hint": "schlagwoerter",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                }
                            ],
                            "hide_in_detail": false,
                            "hide_in_editor": false,
                            "hide_in_print_dialog": false,
                            "is_preferred": false,
                            "table_id": 6,
                            "table_name_hint": "bilder__schlagwoerter"
                        },
                        "other_table_id": 6,
                        "other_table_name_hint": "bilder__schlagwoerter",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 17,
                        "column_name_hint": "objekte",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "inline": "standard",
                        "kind": "link",
                        "mask_id": "PREFERRED",
                        "other_table_id": 8,
                        "other_table_name_hint": "objekte",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 18,
                        "column_name_hint": "reference",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "off"
                        },
                        "kind": "field",
                        "output": {
                            "detail": false,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": false,
                            "text": false
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": false,
                            "nested": false
                        }
                    }
                ],
                "hide_in_detail": false,
                "hide_in_editor": false,
                "hide_in_print_dialog": false,
                "is_preferred": true,
                "mask_id": 4,
                "name": "bilder__all_fields",
                "require_comment": "never",
                "system_fields": {
                    "acl": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "collections": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "object_id": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "owner": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "parent": {
                        "edit": {
                            "mode": "off"
                        },
                        "inline": "standard",
                        "mask_id": "PREFERRED",
                        "output": {
                            "mode": "off"
                        }
                    },
                    "pool": {
                        "output": {
                            "mode": "show"
                        }
                    },
                    "publish": {
                        "output": {
                            "mode": "off"
                        }
                    },
                    "tags": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    }
                },
                "table_id": 4,
                "table_name_hint": "bilder"
            },
            {
                "comment": "",
                "fields": [
                    {
                        "column_id": 15,
                        "column_name_hint": "inventarnummer",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma",
                                "order": 1
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "column_id": 16,
                        "column_name_hint": "datierung",
                        "custom_settings": {},
                        "edit": {
                            "group_edit": false,
                            "mode": "edit"
                        },
                        "kind": "field",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    },
                    {
                        "custom_settings": {},
                        "edit": {
                            "append_only": false,
                            "as_table": false,
                            "mode": "edit",
                            "show_labels": false
                        },
                        "kind": "reverse-linked-table",
                        "mask": {
                            "comment": "",
                            "fields": [
                                {
                                    "column_id": 5,
                                    "column_name_hint": "datei",
                                    "custom_settings": {
                                        "show_in_map": true
                                    },
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {
                                            "order": 1
                                        },
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 6,
                                    "column_name_hint": "titel",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 7,
                                    "column_name_hint": "beschreibung",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 8,
                                    "column_name_hint": "aufnahmedatum",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 9,
                                    "column_name_hint": "aufnahmeort",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "edit"
                                    },
                                    "inline": "standard",
                                    "kind": "link",
                                    "mask_id": "PREFERRED",
                                    "other_table_id": 2,
                                    "other_table_name_hint": "orte",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "custom_settings": {},
                                    "edit": {
                                        "append_only": false,
                                        "as_table": false,
                                        "mode": "edit",
                                        "show_labels": false
                                    },
                                    "kind": "linked-table",
                                    "mask": {
                                        "comment": "",
                                        "fields": [
                                            {
                                                "column_id": 10,
                                                "column_name_hint": "person",
                                                "custom_settings": {},
                                                "edit": {
                                                    "group_edit": false,
                                                    "mode": "edit"
                                                },
                                                "inline": "standard",
                                                "kind": "link",
                                                "mask_id": "PREFERRED",
                                                "other_table_id": 1,
                                                "other_table_name_hint": "personen",
                                                "output": {
                                                    "detail": true,
                                                    "standard": {
                                                        "design": "normal",
                                                        "format": "comma"
                                                    },
                                                    "standard_eas": {},
                                                    "table": true,
                                                    "text": true
                                                },
                                                "search": {
                                                    "expert": true,
                                                    "facet": true,
                                                    "fulltext": true,
                                                    "nested": false
                                                }
                                            },
                                            {
                                                "column_id": 11,
                                                "column_name_hint": "bemerkung",
                                                "custom_settings": {},
                                                "edit": {
                                                    "group_edit": false,
                                                    "mode": "edit"
                                                },
                                                "kind": "field",
                                                "output": {
                                                    "detail": true,
                                                    "standard": {
                                                        "design": "normal",
                                                        "format": "comma"
                                                    },
                                                    "standard_eas": {},
                                                    "table": true,
                                                    "text": true
                                                },
                                                "search": {
                                                    "expert": true,
                                                    "facet": true,
                                                    "fulltext": true,
                                                    "nested": false
                                                }
                                            }
                                        ],
                                        "hide_in_detail": false,
                                        "hide_in_editor": false,
                                        "hide_in_print_dialog": false,
                                        "is_preferred": false,
                                        "table_id": 5,
                                        "table_name_hint": "bilder__personen"
                                    },
                                    "other_table_id": 5,
                                    "other_table_name_hint": "bilder__personen",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "custom_settings": {},
                                    "edit": {
                                        "append_only": false,
                                        "as_table": false,
                                        "mode": "edit",
                                        "show_labels": false
                                    },
                                    "kind": "linked-table",
                                    "mask": {
                                        "comment": "",
                                        "fields": [
                                            {
                                                "column_id": 12,
                                                "column_name_hint": "schlagwort",
                                                "custom_settings": {},
                                                "edit": {
                                                    "group_edit": false,
                                                    "mode": "edit"
                                                },
                                                "inline": "standard",
                                                "kind": "link",
                                                "mask_id": "PREFERRED",
                                                "other_table_id": 3,
                                                "other_table_name_hint": "schlagwoerter",
                                                "output": {
                                                    "detail": true,
                                                    "standard": {
                                                        "design": "normal",
                                                        "format": "comma"
                                                    },
                                                    "standard_eas": {},
                                                    "table": true,
                                                    "text": true
                                                },
                                                "search": {
                                                    "expert": true,
                                                    "facet": true,
                                                    "fulltext": true,
                                                    "nested": false
                                                }
                                            }
                                        ],
                                        "hide_in_detail": false,
                                        "hide_in_editor": false,
                                        "hide_in_print_dialog": false,
                                        "is_preferred": false,
                                        "table_id": 6,
                                        "table_name_hint": "bilder__schlagwoerter"
                                    },
                                    "other_table_id": 6,
                                    "other_table_name_hint": "bilder__schlagwoerter",
                                    "output": {
                                        "detail": true,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": true,
                                        "text": true
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": true,
                                        "fulltext": true,
                                        "nested": false
                                    }
                                },
                                {
                                    "column_id": 18,
                                    "column_name_hint": "reference",
                                    "custom_settings": {},
                                    "edit": {
                                        "group_edit": false,
                                        "mode": "off"
                                    },
                                    "kind": "field",
                                    "output": {
                                        "detail": false,
                                        "standard": {
                                            "design": "normal",
                                            "format": "comma"
                                        },
                                        "standard_eas": {},
                                        "table": false,
                                        "text": false
                                    },
                                    "search": {
                                        "expert": true,
                                        "facet": false,
                                        "fulltext": false,
                                        "nested": false
                                    }
                                }
                            ],
                            "hide_in_detail": false,
                            "hide_in_editor": false,
                            "hide_in_print_dialog": false,
                            "is_preferred": false,
                            "table_id": 4,
                            "table_name_hint": "bilder"
                        },
                        "other_column_id": 17,
                        "other_column_name_hint": "objekte",
                        "other_table_id": 4,
                        "other_table_name_hint": "bilder",
                        "output": {
                            "detail": true,
                            "standard": {
                                "design": "normal",
                                "format": "comma"
                            },
                            "standard_eas": {},
                            "table": true,
                            "text": true
                        },
                        "search": {
                            "expert": true,
                            "facet": true,
                            "fulltext": true,
                            "nested": false
                        }
                    }
                ],
                "hide_in_detail": false,
                "hide_in_editor": false,
                "hide_in_print_dialog": false,
                "is_preferred": true,
                "mask_id": 6,
                "name": "objekte__all_fields",
                "require_comment": "never",
                "system_fields": {
                    "acl": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    },
                    "collections": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "object_id": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "owner": {
                        "edit": {
                            "mode": "off"
                        },
                        "output": {
                            "mode": "off"
                        }
                    },
                    "parent": {
                        "edit": {
                            "mode": "off"
                        },
                        "inline": "standard",
                        "mask_id": "PREFERRED",
                        "output": {
                            "mode": "off"
                        }
                    },
                    "pool": {
                        "output": {
                            "mode": "show"
                        }
                    },
                    "publish": {
                        "output": {
                            "mode": "off"
                        }
                    },
                    "tags": {
                        "edit": {
                            "mode": "edit"
                        },
                        "output": {
                            "mode": "show"
                        }
                    }
                },
                "table_id": 8,
                "table_name_hint": "objekte"
            }
        ],
        "max_mask_id": 6,
        "type": "user",
        "version": 1
    },
    "keys": {
        "mask.1.personen__all_fields.1.field.1.edit_user_hint": {
            "_comment": "personen.name",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.1.personen__all_fields.1.field.1.output_user_hint": {
            "_comment": "personen.name",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.1.personen__all_fields.1.field.2.edit_user_hint": {
            "_comment": "personen.adresse",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.1.personen__all_fields.1.field.2.output_user_hint": {
            "_comment": "personen.adresse",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.2.orte__all_fields.2.field.3.edit_user_hint": {
            "_comment": "orte.name",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.2.orte__all_fields.2.field.3.output_user_hint": {
            "_comment": "orte.name",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.3.schlagworte__all_fields.3.field.4.edit_user_hint": {
            "_comment": "schlagwoerter.name",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.3.schlagworte__all_fields.3.field.4.output_user_hint": {
            "_comment": "schlagwoerter.name",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.18.edit_user_hint": {
            "_comment": "bilder.reference",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.18.output_user_hint": {
            "_comment": "bilder.reference",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.5.edit_user_hint": {
            "_comment": "bilder.datei",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.5.output_user_hint": {
            "_comment": "bilder.datei",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.6.edit_user_hint": {
            "_comment": "bilder.titel",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.6.output_user_hint": {
            "_comment": "bilder.titel",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.7.edit_user_hint": {
            "_comment": "bilder.beschreibung",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.7.output_user_hint": {
            "_comment": "bilder.beschreibung",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.8.edit_user_hint": {
            "_comment": "bilder.aufnahmedatum",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.field.8.output_user_hint": {
            "_comment": "bilder.aufnahmedatum",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.link.17.edit_user_hint": {
            "_comment": "bilder.objekte",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.link.17.output_user_hint": {
            "_comment": "bilder.objekte",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.link.9.edit_user_hint": {
            "_comment": "bilder.aufnahmeort",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.link.9.output_user_hint": {
            "_comment": "bilder.aufnahmeort",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.linked-table.5.edit_user_hint": {
            "_comment": "bilder.bilder__personen",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.linked-table.5.output_user_hint": {
            "_comment": "bilder.bilder__personen",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.linked-table.6.edit_user_hint": {
            "_comment": "bilder.bilder__schlagwoerter",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.4.linked-table.6.output_user_hint": {
            "_comment": "bilder.bilder__schlagwoerter",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.5.mask_4.field.11.edit_user_hint": {
            "_comment": "bilder.bilder__personen.bemerkung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.5.mask_4.field.11.output_user_hint": {
            "_comment": "bilder.bilder__personen.bemerkung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.5.mask_4.link.10.edit_user_hint": {
            "_comment": "bilder.bilder__personen.person",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.5.mask_4.link.10.output_user_hint": {
            "_comment": "bilder.bilder__personen.person",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.6.mask_4.link.12.edit_user_hint": {
            "_comment": "bilder.bilder__schlagwoerter.schlagwort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.4.bilder__all_fields.6.mask_4.link.12.output_user_hint": {
            "_comment": "bilder.bilder__schlagwoerter.schlagwort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.18.edit_user_hint": {
            "_comment": "objekte.bilder.reference",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.18.output_user_hint": {
            "_comment": "objekte.bilder.reference",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.5.edit_user_hint": {
            "_comment": "objekte.bilder.datei",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.5.output_user_hint": {
            "_comment": "objekte.bilder.datei",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.6.edit_user_hint": {
            "_comment": "objekte.bilder.titel",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.6.output_user_hint": {
            "_comment": "objekte.bilder.titel",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.7.edit_user_hint": {
            "_comment": "objekte.bilder.beschreibung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.7.output_user_hint": {
            "_comment": "objekte.bilder.beschreibung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.8.edit_user_hint": {
            "_comment": "objekte.bilder.aufnahmedatum",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.field.8.output_user_hint": {
            "_comment": "objekte.bilder.aufnahmedatum",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.link.9.edit_user_hint": {
            "_comment": "objekte.bilder.aufnahmeort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4.mask_8.link.9.output_user_hint": {
            "_comment": "objekte.bilder.aufnahmeort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4mask_8..linked-table.5.edit_user_hint": {
            "_comment": "objekte.bilder.bilder__personen",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4mask_8..linked-table.5.output_user_hint": {
            "_comment": "objekte.bilder.bilder__personen",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4mask_8..linked-table.6.edit_user_hint": {
            "_comment": "objekte.bilder.bilder__schlagwoerter",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.4mask_8..linked-table.6.output_user_hint": {
            "_comment": "objekte.bilder.bilder__schlagwoerter",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.5.mask_8.mask_4.field.11.edit_user_hint": {
            "_comment": "objekte.bilder.bilder__personen.bemerkung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.5.mask_8.mask_4.field.11.output_user_hint": {
            "_comment": "objekte.bilder.bilder__personen.bemerkung",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.5.mask_8.mask_4.link.10.edit_user_hint": {
            "_comment": "objekte.bilder.bilder__personen.person",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.5.mask_8.mask_4.link.10.output_user_hint": {
            "_comment": "objekte.bilder.bilder__personen.person",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.6.mask_8.mask_4.link.12.edit_user_hint": {
            "_comment": "objekte.bilder.bilder__schlagwoerter.schlagwort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.6.mask_8.mask_4.link.12.output_user_hint": {
            "_comment": "objekte.bilder.bilder__schlagwoerter.schlagwort",
            "de-DE": "",
            "en-US": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.field.15.edit_user_hint": {
            "_comment": "objekte.inventarnummer",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.field.15.output_user_hint": {
            "_comment": "objekte.inventarnummer",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.field.16.edit_user_hint": {
            "_comment": "objekte.datierung",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.field.16.output_user_hint": {
            "_comment": "objekte.datierung",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.reverse-linked-table.4.edit_user_hint": {
            "_comment": "objekte.bilder",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "mask.8.objekte__all_fields.8.reverse-linked-table.4.output_user_hint": {
            "_comment": "objekte.bilder",
            "de-DE": "",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.aufnahmedatum": {
            "_comment": "",
            "de-DE": "Aufnahmedatum",
            "en-US": "date",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.aufnahmeort": {
            "_comment": "",
            "de-DE": "Aufnahmeort",
            "en-US": "location",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.beschreibung": {
            "_comment": "",
            "de-DE": "Beschreibung",
            "en-US": "description",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.bilder__personen": {
            "_comment": "",
            "de-DE": "Personen",
            "en-US": "persons",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.bilder__schlagwoerter": {
            "_comment": "",
            "de-DE": "Schlagwörter",
            "en-US": "keywords",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.datei": {
            "_comment": "",
            "de-DE": "Datei",
            "en-US": "file",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.objekte": {
            "_comment": "",
            "de-DE": "Objekte",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.column.titel": {
            "_comment": "",
            "de-DE": "Titel",
            "en-US": "title",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder.name": {
            "_comment": "",
            "de-DE": "Bilder",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.bilder__personen.column.bemerkung": {
            "_comment": "",
            "de-DE": "Bemerkung",
            "en-US": "remark",
            "it-IT": ""
        },
        "schema.bilder__personen.column.person": {
            "_comment": "",
            "de-DE": "Person",
            "en-US": "person",
            "it-IT": ""
        },
        "schema.bilder__personen.name": {
            "_comment": "",
            "de-DE": "Personen",
            "en-US": "persons",
            "it-IT": ""
        },
        "schema.bilder__schlagwoerter.column.schlagwort": {
            "_comment": "",
            "de-DE": "Schlagwort",
            "en-US": "keyword",
            "it-IT": ""
        },
        "schema.bilder__schlagwoerter.name": {
            "_comment": "",
            "de-DE": "Schlagwörter",
            "en-US": "keywords",
            "it-IT": ""
        },
        "schema.objekte.column.datierung": {
            "_comment": "",
            "de-DE": "Datierung",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.objekte.column.inventarnummer": {
            "_comment": "",
            "de-DE": "Inventarnummer",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.objekte.column.reverse:bilder.17": {
            "_comment": "",
            "de-DE": "Bilder",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.objekte.name": {
            "_comment": "",
            "de-DE": "Objekte",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.orte.column.name": {
            "_comment": "",
            "de-DE": "Name",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.orte.name": {
            "_comment": "",
            "de-DE": "Orte",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.personen.column.adresse": {
            "_comment": "",
            "de-DE": "Adresse",
            "en-US": "address",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.personen.column.name": {
            "_comment": "",
            "de-DE": "Name",
            "en-US": "name",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.personen.name": {
            "_comment": "",
            "de-DE": "Personen",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.schlagwoerter.column.name": {
            "_comment": "",
            "de-DE": "Name",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        },
        "schema.schlagwoerter.name": {
            "_comment": "",
            "de-DE": "Schlagwörter",
            "en-US": "",
            "es-ES": "",
            "it-IT": ""
        }
    }
}
```