# Rejected findings, Gitea

Findings the official grader could not match, that our review rejected. Each counts as incorrect in its run.

| Kind | Bugs |
|---|---|
| Behavior Gitea chose in its code | 48 |
| The agent was wrong (test procedure, evidence, or test environment) | 21 |
| Address or input the app never produces | 6 |

## Behavior Gitea chose in its code (48)

| Area | Id | Bug | Why |
|---|---|---|---|
| issues | issues-5 | Issue search for an emoji that is in a title returns no results | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| issues | issues-6 | "Words" search mode needs all words in the same field (title, body or comments) | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| issues | issues-7 | Time Tracker sidebar block shows only its heading and gear when no time is tracked | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| issues | issues-16 | Back to the new-issue form restores the body but not the Title | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| issues | issues-17 | Dashboard/org Issues: left-hand section counters do not follow the Author and Assignee filters | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| labels | labels-9 | "Least issues" label sort orders by total issues while the row shows only open issues | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| milestones | milestones-3 | Saving a stale milestone edit form in a second tab overwrites the title and due date saved in the first tab (last write wins) | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| notifications | notifications-4 | After sign-out, browser Back shows the cached signed-in notifications page | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| notifications | notifications-5 | Pinning a notification clears its unread count | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| profiles-account-settings | profiles-1 | "Update Avatar" with no file chosen answers "Your avatar has been updated." | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| profiles-account-settings | profiles-6 | Blocking an already blocked user answers "Failed to block user: cannot block the user" | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| profiles-account-settings | profiles-9 | "Unblock" on a blocked user's profile opens the blocked-users settings page instead of unblocking | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| profiles-account-settings | profiles-11 (accessibility) | "admin" label overlaps the avatar in the top navigation | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| profiles-account-settings | profiles-17 | Browser Back after signing out shows the previous settings page again | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| pull-requests | pull-requests-7 | Changing a pull request's target branch re-creates the 'added 1 commit' event at the end of the timeline with a new time | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| pull-requests | pull-requests-9 | Author filter on the global pull request list keeps the label 'Author' and shows the chosen user only as prefilled search text | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| pull-requests | pull-requests-10 | Dashboard sidebar counters ('In your repositories', 'Created by you') do not follow the Author filter | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| pull-requests | pull-requests-15 | After signing out, the browser Back button shows the previously viewed private pull request pages | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-3 | Tag page of v1.0.0 has no edit pencil | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-4 | Archive download link of a missing tag answers a plain-text 404 line instead of the styled 404 page | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-5 | New Release helper says 'New tag. This tag will be created from the target.' for the tag name of an existing draft release | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-7 | Saving a draft release moves its date to the save time and puts it first in the list | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-11 | Tag name on a draft release card is a link with href="#" | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-16 | /releases/new?tag=<name> opens pre-filled with the existing release's title and notes | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-17 (accessibility) | Escape in the target-branch dropdown keeps the option reached with the arrow keys | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-18 (accessibility) | 64-character tag name is cut off in the tags list at 390 px | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| releases | releases-20 | Draft release saved with a new tag name does not create the tag | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-code | repository-code-3 | Apply Patch commits an empty file when the pasted diff has a new-file header but no hunk | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-code | repository-code-4 | Archive download for a non-existent tag answers a plain-text 404 "unrecognized repository reference" | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-code | repository-code-5 | Commit search results do not show the tag badge that the plain commit list shows | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-code | repository-code-21 | Branches list shows "eval" next to a branch whose latest commit was authored by Alex Rivera | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-code | repository-code-22 | Code search for a term starting with "-" ("-i") returns lines that do not contain it | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-settings | repository-settings-3 | A private repository keeps 'Anonymous Read' and shows both 'Private' and 'Public Access' badges | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-settings | repository-settings-6 (accessibility) | Escape does not close the 'Delete Branch Protection' confirm dialog | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-settings | repository-settings-7 | After sign-out the browser Back button re-displays the cached repository Settings page | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-settings | repository-settings-9 | Creating a branch protection rule reports 'Branch protection for rule ... has been updated' | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| repository-settings | repository-settings-10 | Push-mirror address without a scheme answers 'You are not allowed to import local repositories.' | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-6 | After sign-out, browser Back re-displays the cached admin User Accounts page | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-7 | Queue pool settings accept -1 as 'Max Number of workers' | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-8 | Submitting an empty 'Max Number of workers' shows 'Settings Updated' and keeps the value | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-11 | 'Update Avatar' with no file chosen reports 'The user's avatar has been updated.' | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-12 (accessibility) | 'admin' badge overlaps the account avatar in the mobile navigation menu | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| site-administration | site-administration-18 | A nonexistent admin user address (/-/admin/users/999) redirects to the user list instead of a Not Found page | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| wiki | wiki-10 | Home page's "Glossary" link opens the Pages list because no Glossary page exists | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| wiki | wiki-11 | "View original Git file" (.md) link on the Pages list opens the rendered page, not raw Markdown | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| wiki | wiki-13 | Relative links and image paths on a page with a slash in its title resolve against the wiki root | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| wiki | wiki-14 | Commit diff and downloaded .diff show an accented wiki file name percent-encoded | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |
| wiki | wiki-18 | A wiki page re-created under a deleted page's name shows the old page's revisions | behaviour is deliberate in Gitea 1.24.7 (see reason and source) |

## The agent was wrong (test procedure, evidence, or test environment) (21)

| Area | Id | Bug | Why |
|---|---|---|---|
| issues | issues-1 | Assignees picker: ticks, unticks and "Clear assignees" are only sent when the picker closes (reload with it open loses them) | test procedure: page reloaded with the picker still open (Gitea saves on close) |
| issues | issues-9 | Long line in a fenced code block is clipped at the block edge; page claimed to scroll sideways | evidence does not show the claim (page not wider) |
| issues | issues-11 | Double-clicking the bulk "Close" button: second request reported to answer 500 (intermittent) | environment: intermittent, no visible effect |
| issues | issues-12 | Search mode picked in the dropdown (Fuzzy) is lost when another dashboard section is clicked | test procedure: search mode changed but the search was never submitted |
| labels | labels-2 | Ticking a label in the sidebar Labels picker is only saved when the picker closes | test procedure: page reloaded with the picker still open (Gitea saves on close) |
| labels | labels-3 | "Exclusive" checkbox cannot be ticked in the New/Edit Label dialog | test procedure: label name without a scope; the dialog explains the requirement |
| milestones | milestones-1 | New Milestone: pressing Enter in Title raises the browser leave-page prompt; if dismissed, nothing is created | environment: automation key timing (instant key press) |
| profiles-account-settings | profiles-10 | Profile RSS feed claimed to be served as text/html and shown as escaped markup | evidence contradicts the claim (the feed is XML) |
| profiles-account-settings | profiles-14 | Private profile's RSS feed (/eval.rss) readable by a user who gets 404 on the profile page | not proven: visibility and signed-in user not shown; profile edited in parallel |
| profiles-account-settings | profiles-16 | Biography longer than 255 characters ends up cut to 255 with a success message | evidence contradicts the claim (the field has maxlength) |
| pull-requests | pull-requests-12 | Assignee picked in the sidebar dropdown is not saved | test procedure: page reloaded with the picker still open (Gitea saves on close) |
| releases | releases-9 | Releases RSS feed has no items | test procedure: a plain tag was taken for a release |
| releases | releases-12 | Release notes table with a 155-character unbroken cell is clipped at 390 px | test procedure: the table's own horizontal scroll was not tried |
| repository-code | repository-code-20 | Apply Patch answers "The file contents have changed since you started editing" on the first Commit Changes click | environment: other agents were pushing to the same branch |
| site-administration | site-administration-9 | Admin tables are clipped at 768 px with no visible scrollbar (queue detail table, repository list) | test procedure: the panel's own horizontal scroll was not tried |
| site-administration | site-administration-13 | Pressing Enter on the New Organization form triggers a 'Leave site?' prompt and no validation message | environment: automation key timing (instant key press) |
| site-administration | site-administration-15 | Dashboard update banner announces 'Gitea 28.4.0' while the instance runs 1.24.7 | environment: the banner shows what Gitea's update server returns |
| wiki | wiki-9 | Escape on the editor's table-size popup raises a JavaScript error banner and does not close the popup | not reproduced: the reproduction video and the owner's check show no error |
| wiki | wiki-12 | The "Aa" monospace toggle in the wiki editor changes nothing visible | evidence contradicts the claim (the font does change) |
| wiki | wiki-16 | Wide Markdown tables in wiki content and in _Sidebar are cut off with no scroll area of their own | test procedure: the table's own horizontal scroll was not tried |
| wiki | wiki-17 | A wiki address containing %00 returns a blank 400 page | environment: the sandbox proxy answers, not Gitea |

## Address or input the app never produces (6)

| Area | Id | Bug | Why |
|---|---|---|---|
| issues | issues-10 | New-issue link ignores ?labels= and ?assignee= parameters | query parameters Gitea does not offer |
| profiles-account-settings | profiles-4 | /<user>?tab=packages shows the repository list with no tab highlighted | hand-typed ?tab= value |
| pull-requests | pull-requests-2 | Global /pulls with sort=newest is ordered like Recently updated | hand-typed ?sort= value |
| pull-requests | pull-requests-11 | Global /pulls with state=all lists only open pull requests | hand-typed ?state= value |
| repository-code | repository-code-17 | Delete page renders the delete form for a file path that does not exist | hand-typed path of a missing file |
| wiki | wiki-15 | Hand-typed .md address of an accented wiki page shows the Pages list | hand-typed .md address |
