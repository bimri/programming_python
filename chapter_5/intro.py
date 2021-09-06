"Telling the Monkeys What to Do"
'''
Most computers spend a lot of time doing nothing. If you start a system monitor tool
and watch the CPU utilization, you’ll see what I mean—it’s rare to see one hit 100
percent, even when you are running multiple programs. *There are j ust t oo many del ays
built into software: disk accesses, network traffic, database queries, waiting for users
to click a button, and so on. In fact, the majority of a modern CPU’s capacity is often
spent in an idle state; faster chips help speed up performance demand peaks, but much
of their power can go largely unused.

Early on in computing, programmers realized that they could tap into such unused
processing power by running more than one program at the same time. By dividing the
CPU’s attention among a set of tasks, its capacity need not go to waste while any given
task is waiting for an external event to occur. The technique is usually called parallel
processing (and sometimes “multiprocessing” or even “multitasking”) because many
tasks seem to be performed at once, overlapping and parallel in time. It’s at the heart
of modern operating systems, and it gave rise to the notion of multiple-active-window
computer interfaces we’ve all come to take for granted. Even within a single program,
dividing processing into tasks that run in parallel can make the overall system faster,
at least as measured by the clock on your wall.

There are two fundamental ways to get tasks running at the same time in Python—
process forks and spawned threads. Functionally, both rely on underlying operating
system services to run bits of Python code in parallel. Procedurally, they are very different
in terms of interface, portability, and communication. For instance, at this writing
direct process forks are not supported on Windows under standard Python (though
they are under Cygwin Python on Windows).

By contrast, Python’s thread support works on all major platforms. Moreover, the
os.spawn family of calls provides additional ways to launch programs in a platformneutral
way that is similar to forks, and the os.popen and os.system calls and
subprocess module we studied in Chapters 2 and 3 can be used to portably spawn
programs with shell commands. The newer multiprocessing module offers additional
ways to run processes portably in many contexts.

One note up front: although the process, thread, and IPC mechanisms we will explore
in this chapter are the primary parallel processing tools in Python scripts, the third party
domain offers additional options which may serve more advanced or specialized roles.
As just one example, the MPI for Python system allows Python scripts to also employ
the Message Passing Interface (MPI) standard, allowing Python programs to exploit
multiple processors in various ways.
'''
