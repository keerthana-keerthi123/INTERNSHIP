class InstagramAccount:
    def __init__(self, account_name, password):
        # Public variable
        self.account_name = account_name
        
        # Protected variable
        self._private_reels = []
        
        # Private variable
        self.__archived_reels = []
        
        # Private password
        self.__password = password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels (only for followers)
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels (password required)
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter method for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Wrong password"

    # 6. Setter method to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully!")
        else:
            print("Password update failed! Wrong old password.")
