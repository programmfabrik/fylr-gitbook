# White papers

The concept pages explain fylr's vocabulary. The white papers in this section go one level deeper: each one is the design document behind a fylr subsystem — the problem it replaces, the alternatives that were rejected, and why the built design looks the way it does. They are written at implementation time and kept as the durable record of the reasoning.

Read them when you operate fylr at scale, debug the subsystem they describe, or want to understand a design decision that the reference documentation states but does not argue.

* [Execserver slot broker](execserver-slot-broker.md) — how fylr servers and execservers negotiate job slots over a websocket instead of polling, and why that retires the token handshake.
* [Plugin shop and secure delivery](secure-plugin-delivery.md) — how paid plugins reach the customers entitled to them: a configurable source list for discovery, and an encrypted package unlocked through the license for delivery.
