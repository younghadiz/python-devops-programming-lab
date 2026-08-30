"""Exercise 10: Fetch public GitHub repositories."""

import requests


GITHUB_API_URL = "https://api.github.com"
REQUEST_TIMEOUT_SECONDS = 10


def get_public_repositories(username: str) -> list[dict]:
    endpoint = (
        f"{GITHUB_API_URL}/users/{username}/repos"
    )

    params = {
        "type": "owner",
        "sort": "updated",
        "direction": "desc",
        "per_page": 100,
    }

    headers = {
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(
        endpoint,
        params=params,
        headers=headers,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    response.raise_for_status()

    return response.json()


def main() -> None:
    username = input(
        "Enter a GitHub username: "
    ).strip()

    if not username:
        print("GitHub username cannot be empty.")
        return

    try:
        repositories = get_public_repositories(
            username
        )
    except requests.exceptions.Timeout:
        print("GitHub API request timed out.")
        return
    except requests.exceptions.ConnectionError:
        print("Unable to connect to GitHub.")
        return
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        if status_code == 404:
            print(
                f"GitHub user '{username}' was not found."
            )
        else:
            print(
                f"GitHub API returned HTTP "
                f"{status_code}."
            )

        return
    except requests.exceptions.RequestException as error:
        print(f"GitHub API request failed: {error}")
        return

    if not repositories:
        print(
            f"No public repositories found for "
            f"{username}."
        )
        return

    print(
        f"\nPublic repositories for {username}:"
    )

    for repository in repositories:
        print(
            f"\nName: {repository['name']}\n"
            f"URL:  {repository['html_url']}"
        )


if __name__ == "__main__":
    main()