from dataclasses import dataclass

# One Freelance order template
# An order has a title, a description, and it's own price.
# To make it easier for the AI, currency is a separate thing.
@dataclass
class Order:
    title: str
    description: str
    price: float
    currency: str = "KZT" # byDefault


# A freelancer should have their own profile
# Basing on this data, the AI can make it's decisions
# TODO: Make this unneccessary to have.
@dataclass
class FreelancerProfile:
    name: str
    specialization: str
    skills: list[str] # Skills is a list. You can have multiple skills the AI can base off from.
    experience: str = ""