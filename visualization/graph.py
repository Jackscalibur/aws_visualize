from pyvis.network import Network

def create_aws_network(services):
    """
    Create a network graph where each node represents an AWS service.

    :param services: A dictionary where keys are service names and values are lists of related services.
    """
    net = Network(height="750px", width="100%", directed=True)

    # Add nodes
    for service in services:
        net.add_node(service, label=service, title=f"AWS Service: {service}")

    # Add edges
    for service, related_services in services.items():
        for related_service in related_services:
            net.add_edge(service, related_service)
    
    net.set_options("""
    var options = {
      "nodes": {
        "shape": "dot",
        "size": 20
      },
      "edges": {
        "arrows": {
          "to": {
            "enabled": true
          }
        }
      },
      "physics": {
        "enabled": true
      }
    }
    """)
    net.show("aws_network.html")

