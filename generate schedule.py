 def generate_schedule(self, env):
        self.policy_est.load_state_dict(torch.load(self.settings['DATA_PATH'] + '/actor_final.pt'))
        self.value_est.load_state_dict(torch.load(self.settings['DATA_PATH'] + '/critic_final.pt'))

        env.reset()
        self.schedule = None
        done = False

        while not done:
            state = env.get_current_state()
            action = self.policy_est.predict(state)
            self.schedule = env.step(action)
            done = env.is_done()

        total_reward = env.get_total_reward()
        print("Generated Schedule:", self.schedule)
        print("Total Reward for the Generated Schedule:", total_reward)

        return self.schedule, total_reward