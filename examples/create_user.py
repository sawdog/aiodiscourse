import asyncio

from common import get_discourse_client

async def main():
    async with get_discourse_client() as client:
        # If registrations are turned off ...
        # One can turn off registration to stop signups locally.
        # That blocks creating new users, so toggle to turn on registration
        await client.admin.set_site_setting("allow_new_registrations", True)

        # Now Create a user
        user = await client.users.create(
                email="testuser@mydomain.com",
                username="testuser",
                name="Test User",
                password="My123T3stP@ssw0rd",
                active=True,
                approved=True,
                )
        user_id = user.get("user_id") or user.get("id")
        # Approve them (if approval is required)
        if user_id:
            await client.admin.approve_user(user_id)
            print(f"Approved new user ID: {user_id}")

        # now we turn back off registrations.....
        await client.admin.set_site_setting("allow_new_registrations", False)


asyncio.run(main())

