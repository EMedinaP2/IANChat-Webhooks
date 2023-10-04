from google.cloud import dialogflowcx_v3
parent = "projects/ml-testtool-desa/locations/global/agents/5505faeb-9005-46e0-a677-b09c434a24dc"


def sample_create_entity_type(name,entities):
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()
    # Initialize request argument(s)
    entity_type = dialogflowcx_v3.EntityType()
    entity_type.display_name = name
    entity_type.kind = "KIND_MAP"
    entity_type.entities = entities

    request = dialogflowcx_v3.CreateEntityTypeRequest(
        parent=parent,
        entity_type=entity_type,
        language_code="es"

    )

    # Make the request
    response = client.create_entity_type(request=request)

    # Handle the response
    return response


def sample_update_entity_type(name, entities):
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()

    # Initialize request argument(s)
    entity_type = dialogflowcx_v3.EntityType()
    entity_type.name = parent + f"/entityTypes/{name}"
    entity_type.display_name = "products2"
    entity_type.kind = "KIND_MAP"
    entity_type.entities = entities
    print(entity_type)
    request = dialogflowcx_v3.UpdateEntityTypeRequest(
        entity_type=entity_type,
        language_code = "es"
    )

    # Make the request
    response = client.update_entity_type(request=request)

    # Handle the response
    return response


def sample_list_entity_types():
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()

    # Initialize request argument(s)
    request = dialogflowcx_v3.ListEntityTypesRequest(
        parent=parent,
        language_code="es"
    )

    # Make the request
    page_result = client.list_entity_types(request=request)

    # Handle the response
    return page_result


def sample_get_entity_type(name):
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()

    # Initialize request argument(s)
    request = dialogflowcx_v3.GetEntityTypeRequest(
        name=parent + f"/entityTypes/{name}",
        language_code="es"
    )
    # Make the request
    response = client.get_entity_type(request=request)
    return response
