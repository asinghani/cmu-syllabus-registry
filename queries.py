from gql import gql

def syllabus_registry():
    return gql(
        """
        query MyQuery {
            course(sisId: "syllabus-registry") {
                sisId
                state
                name
                modulesConnection {
                    nodes {
                        _id
                        name
                        moduleItems {
                            content {
                                ... on ExternalUrl {
                                    title
                                    url
                                }
                            }
                        }
                    }
                }
            }
        }
        """
    )

def get_syllabi(sis_id):
    return gql(
        """
        query MyQuery {
            course(sisId: \"""" + sis_id + """\") {
                _id
                state
                name
                modulesConnection {
                    nodes {
                        _id
                        name
                        moduleItems {
                            content {
                                ... on Page {
                                    id
                                    title
                                    _id
                                }
                                ... on File {
                                    id
                                    displayName
                                    url
                                }
                            }
                            _id
                        }
                    }
                }
            }
        }
        """
    )