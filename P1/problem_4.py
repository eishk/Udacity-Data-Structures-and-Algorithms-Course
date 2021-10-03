class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None:
        return False
    if user in group.get_users():
        return True
    else:
        for g in group.get_groups():
            return is_user_in_group(user, g)
        return False


if __name__ == "__main__":
    #Example given
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    non_child_user = ""
    child.add_group(sub_child)
    parent.add_group(child)
    print(is_user_in_group(sub_child_user, sub_child))
    print(is_user_in_group(sub_child_user, parent))
    print(is_user_in_group(non_child_user, parent))

    first = Group("first")
    second = Group("second")
    third = Group("third")

    third_user = "third_user"
    third.add_user(third_user)
    first.add_group(second)
    second.add_group(third)
    not_user = "not"
    none_user = None
    print(is_user_in_group(third_user, first))
    # Output should be True
    print(is_user_in_group(third_user, second))
    # Output should be True
    print(is_user_in_group(none_user, first))
    # Output should be False
    print(is_user_in_group(not_user, second))
    # Output should be False
