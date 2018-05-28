 def get_playbook_repo_access(username, playbook_repo):
     if username == "admin":
         return True
     result = False
     with open("/usr/local/etc/flansible/rbac.json") as rbac_file:
         rbac_data = json.load(rbac_file)
     user_list = rbac_data['rbac']
     for user in user_list:
         if user['user'] == username:
             ansible_repo_list = user['playbook_repos']
             for repo in ansible_repo_list:
               if str(playbook_repo) == str(repo):
                 result = True
     return result

