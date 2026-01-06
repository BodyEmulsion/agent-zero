import { Api } from "/api.js";
import { store as chatsStore } from "/components/sidebar/chats/chats-store.js";

document.addEventListener('alpine:init', () => {
    Alpine.store('profiles', {
        profileList: [],
        
        async loadProfilesList() {
            const response = await Api.call("profiles", { action: "list" });
            if (response.ok) {
                this.profileList = response.data;
            }
        },

        async setProfile(profileName) {
            const contextId = chatsStore.selectedContextId;
            if (!contextId) return;

            const response = await Api.call("profiles/set", {
                profile: profileName
            });

            if (response.ok) {
                chatsStore.loadContext(contextId);
            }
        },
        
        async createProfile(name) {
             const response = await Api.call("profiles/create", {
                name: name
            });
            if (response.ok) {
                this.loadProfilesList();
                return true;
            }
            return false;
        }
    });
});

export const store = Alpine.store('profiles');
