# Conduit
At it's core, Conduit is a framework for the standardization of test language. Inconsistencies, mistaken command executions, the dreaded skipped step. Conduit wants to keep that from happening again.

## Modules

The way that Conduit resolves these issues is almost by working backwards. Rather than the procedure driving the test, the test is now driving the procedure. Typos, mis-steps, I'm not saying it will make everything better overnight. But I know that personally, I got pretty tired of that level of tedium. I'd rather have the robot do it for me, and I just look at the outputs it spits out.

Different modules can be (read: are) slotted into the framework using the same common procedure as the sample ones, CLI (pexpect) and SSH (paramiko).

## Tool Integration

As you develop, you'll find that, more often than not, you're making calls to things that you aren't even really using. The Every custom tool has to have 2 things. A class that defines its available actions and their parameters, and a class that defines any verifiers that it reveals.

The cool thing about that paradigm is that it makes basically a module template. You write out the functions, wrapping your desired effects (actions and verifiers like self.act.* and self.check.*), and define the messages that will be used in the procedure. Easy!

These procedures will get spat out in 2 formats. An HTML document, for human readability, and an XML document for import to downstream aggregators like SonarQube or Jenkins.

## The State of Things

Right now, this program is brand-new. I'm making it up on my own, with a very rudimentary understanding of what needs to be accomplished to achieve this goal. I need to shake off the rust.
