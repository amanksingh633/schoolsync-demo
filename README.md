# SchoolSync: live demo

**[Open the live demo](https://amanksingh633.github.io/schoolsync-demo/)**

SchoolSync is a school management web app (installable PWA) for attendance, fees, academics,
notices and parent communication. This repository hosts a **static demo build** so you can try it
without installing anything.

| Sign in | Teacher roll call | Principal overview |
|---|---|---|
| ![Sign-in screen](screenshots/sign-in.jpg) | ![Teacher roll call](screenshots/roll-call.jpg) | ![Principal overview](screenshots/principal-overview.jpg) |

## How to try it

The demo seeds itself with synthetic data (about 120 students across six classes, six teachers).
Everything runs in your browser; nothing is sent to a server.

**One click:** on the sign-in screen, press **Continue as teacher**, **principal**, **parent** or
**student**. No account or password is needed.

- **Teacher:** pick *Class 6A* to take the roll call, then explore Students, Homework, Notices,
  Timetable, Bulk Marks and the Behaviour Log from the sidebar.
- **Principal:** the school overview, attendance and fee trends, alerts, staff attendance, finance,
  fee structure and grade boundaries.
- **Parent and student:** the family and student views of attendance, homework, fees and notices.
- **Admin views:** *System admin* and *Site admin* links sit under the sign-in form (the site admin
  controls school name and per-module feature toggles).

The regular sign-in (teacher number plus a password you create on first use) still works as well.
Your changes are stored in your browser's local storage, so they stay on your device. Clearing site
data resets the demo.

## Product notes

How I would frame this as a product, and the decisions visible in it. These are design rationale
and hypotheses; nothing here is a measured result, and the demo has had no real-school pilot.

- **Problem.** Schools run attendance, fees, homework and notices across paper registers, chat
  groups and spreadsheets, so nobody has one reliable picture of the day.
- **Users.** Class and subject teachers (daily roll call, marks, homework), the principal
  (overview, approvals, finance), parents and students (what is due, what is owed), and a site
  admin who configures the school.
- **Decisions and trade-offs.**
  - *Role-based home screens*: each user sees only their job, which keeps the interface small but
    means more screens to maintain.
  - *Per-module feature toggles*: a school can adopt gradually instead of switching everything on.
  - *Teacher self check-in needs principal approval*: gives the school an attendance record for
    staff, at the cost of one more step.
  - *Installable and offline-capable (PWA)*: schools often have poor connectivity, so reading and
    working offline matters more than real-time sync.
  - *Records split across documents for 2,000+ students*: simpler to build and cheap to run, but
    it is a scaling shortcut rather than a long-term data model.
  - *Demo-grade sign-in, documented as such*: fast to build and demo, but not acceptable for real
    student data (see the security notes in the app's README).
- **How I would measure it.** Share of classes roll-called by a set time each morning; fee
  collection ageing; share of parents who read a notice; teacher minutes per roll call.
- **Next.** Real authentication with per-role access rules, SMS or chat notifications to parents,
  and fee receipts and exports.
- **Known gaps.** Synthetic data only; no pilot; the sign-in model is the main blocker for real use.

## What's inside

React, Vite, Tailwind CSS and Recharts; offline-capable PWA with a service worker; optional
Firebase Firestore storage for shared multi-device use (switched off in this build). Records are
split across several documents to support 2,000+ students.

## Notes

- This is a demo build of a prototype. Sign-in is checked in the browser and is **not suitable for
  real student or financial data**; please don't enter any.
- The application source lives in a private repository. For contact details, see my
  [GitHub profile](https://github.com/amanksingh633).
- Built with AI assistance (Claude).
