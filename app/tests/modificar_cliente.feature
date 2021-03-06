Feature: Modify a client
    """
        As an Analista de mesa de ayuda,
        I want to modify a cliente
        to be able to correct or change the atributes of a cliente
    """


    Scenario: Success to modify a cliente
        Given I am an Analista de mesa de ayuda and i have a client with razon social: "razon social prueba", CUIT:"123456", descripcion:"descripcion prueba"
        When I modify the razon social por "razon social 2", CUIT:"654321", descripcion: "descripcion modificada"
        Then I can see a cliente With CUIT "654321" and the rest of its atributes modified.

    Scenario: Unuccess to modify a cliente
        Given I am an Analista de mesa de ayuda and i have a client with razon social: "razon social prueba", CUIT:"123456", descripcion:"descripcion prueba"
        When I modify the razon social por "", CUIT:"", descripcion: ""
        Then I see a warning that all the fields must be filled.

    Scenario: Success modification of a client already asigned to a ticket
        Given I have a client and a ticket that already has a client loaded
        When I modify the razon social por "razon social 2", CUIT:"654321", descripcion: "descripcion modificada"
        Then I can see the cliente asigned to the ticket With CUIT "654321" and the rest of its atributes modified.