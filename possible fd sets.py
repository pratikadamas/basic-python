from itertools import chain , combinations

# generat all possible functional dependency sets
def get_subsets(attributes):
    """Generate all non-empty subsets of a given set of attributes."""
    return list(chain.from_iterable(combinations(attributes, r) for r in range(1, len(attributes) + 1)))


def generate_fds(attributes):
    """Generate all possible functional dependencies (FDs) given a set of attributes."""
    subsets = get_subsets(attributes)
    fd_list = []

    for lhs in subsets:
        remaining_attributes = set(attributes) - set(lhs)
        if remaining_attributes:
            rhs_subsets = get_subsets(remaining_attributes)
            for rhs in rhs_subsets:
                fd_list.append((set(lhs), set(rhs)))

    return fd_list


def display_fds(fd_list):
    """Display the generated functional dependencies."""
    for i, (lhs, rhs) in enumerate(fd_list, 1):
        print(f"FD {i}: {', '.join(lhs)} -> {', '.join(rhs)}")


if __name__ == "__main__":
    attributes = input("Enter attributes separated by space: ").split()
    print("\nGenerating all possible functional dependencies:\n")
    fd_list = generate_fds(attributes)
    display_fds(fd_list)
    print(f"\nTotal number of FDs: {len(fd_list)}")
