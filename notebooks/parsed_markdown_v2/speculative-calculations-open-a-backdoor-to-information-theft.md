# speculative-calculations-open-a-backdoor-to-information-theft.html

**Source:** en_news_events/2022/07/speculative-calculations-open-a-backdoor-to-information-theft.html

## Speculative computing makes computers faster

Sometimes a computer bleeds from its heart and reveals droplets of private information. That's the case with the "Retbleed" hardware vulnerability made public today: This vulnerability occurs in the microprocessors that execute the instructions of a computer program and perform the corresponding calculations. In some cases, the processors - namely the central processing units (CPU) - also perform special calculations that shorten the computing time and speed up the overall computing process. In the process, they leave traces in the memory that hackers could exploit to gain unauthorized access to any information in the system - for example, they could steal encryption keys or security-relevant passwords. This is especially risky in cloud environments where multiple companies share computer systems. The National Center for Cyber Security in Bern, Switzerland considers the vulnerability serious because the affected processors are in use worldwide. However, the manufacturers have already taken initial measures to close the vulnerability.

The vulnerability was discovered by the doctoral student Johannes Wikner and Kaveh Razavi, ETH Zurich professor for computer security. The name "Retbleed" refers to a certain type of program instructions, called returns. A computer program consists of sequences of instructions or commands organised into functions with which the processors execute the desired calculations. Once a function has executed, a return instruction causes the processor to return to the point in the computer program immediately after the original instruction that used the function.

## Speculative computing makes computers faster

You can think of the flow of a computer program as a river with various branches. At the branches, computer programs often make decisions about which branch to choose. Sometimes these decisions take a long time and may slow down execution. What is needed, however, are fast computational processes. Traditionally, a computer program executes instructions sequentially and in the program order - that is, one computational step-at-a-time.

## Solution approach for mitigation measures

Today's CPU processor architectures, however, allow computations to be brought forward and executed simultaneously. "A CPU can execute instructions in a different order than the program order to improve computational performance," says Razavi. In computing circles, this is referred to as "out-of-order execution." Since January 2018, it has been known that there can be security vulnerabilities with this type of execution. During instruction execution, unauthorized access to the CPU's cache could occur, allowing hackers to steal sensitive information from the operating system. This vulnerability is known as "Meltdown" and affects specific issues in Intel CPUs.

Closely related to out-of-order execution is "speculative execution," for which similar security issues have also been known since 2018. "'Retbleed' is a speculative execution problem," says Johannes Wikner. Such speculative execution is used to avoid slowing down computations by bringing forward certain computational steps before it is clear whether they are actually needed. Speculative calculations take place, for example, when a processor tries to guess which path the chain of instructions will take at a branch before this is known. "In this process, CPUs 'guess' which direction to take at a branch and speculatively execute instructions based on their guess," Razavi explains.

## Vulnerable return instructions

With the help of such speculations, the flow of the instruction chain is improved and the computing power of the processors is increased. If the speculative calculations are not needed, they are undone. These speculations also leave traces in the cache, which open a backdoor for hackers. This vulnerability was also made public in January 2018 under the name "Spectre" and affects processors from the manufacturers Intel and AMD. Since then, Intel and AMD, as well as major software manufacturers such as Microsoft, have taken mitigation measures. However, the vulnerabilities of the speculative executions have not been conclusively researched or remedied to date.

## Reference

As Wikner and Razavi have now discovered, there is indeed a security problem that has not yet been resolved, "We have shown that with speculative execution, a particularly large number of return statements are vulnerable and can be hijacked," says Wikner. In principle, "Retbleed" works like variant 2 of "Spectre" and affects Intel and AMD microprocessors. "Since the mitigation measures taken so far did not take the return instructions into account, most existing microprocessor computer systems are vulnerable to 'Retbleed'," Razavi adds. "However, it takes some computer expertise to gain memory access and steal information," Wikner says.

In February, Wikner and Razavi provided a proof of concept that “Retbleed” is a serious problem. They have since published their findings in a scientific paper that has been accepted as a USENIX Security 2022 conference paper . In this article, Wikner and Razavi have evaluated Intel and AMD’s first approach to solve the problem. This starts from the fact that when the microprocessor speculates at a branch, the instructions are sometimes executed incorrectly. Then the computation does not lead to the correct destination and opens a leak through which hackers might gain access to the information in the memory. The current solution is to prevent hackers from influencing the microprocessors’ decision on return destinations. Unfortunately, this comes with a substantial performance cost that makes computer 12 to 28 percent slower.

As is usual in such cases, the security researchers first informed the affected manufacturers AMD and Intel before the vulnerability was published. Since the specific security risks also depend on the company-specific processor architecture, the manufacturers got their time to take more in-depth mitigation measures. Since then, Microsoft, Oracle, Google, Linux, Intel, AMD, ARM, among others, have worked on protective measures before "Retbleed" was made public today. An Intel microprocessor that is 3 to 6 years old, or an AMD processor that is 1 to 11 years old, is likely to be affected.

The National Cyber Security Center (NCSC) in Bern, Switzerland has today assigned the CVE numbers CVE-2022-29900 (for processors from the manufacturer AMD) and CVE-2022-29901 (for processors from the manufacturer Intel) for the security vulnerability "Retbleed" in cooperation and in consultation with researchers from ETH Zurich. The assignment of a CVE (Common Vulnerabilities and Exposure) enables a globally unique identification of vulnerabilities. Since September 2021, the NCSC has been recognized as the Swiss approval authority that assigns CVE numbers.

For more information, see the report posted on the NSCS website under the "Advisories" section .

Wikner, J; Razavi, K. RETBLEED: Arbitrary Speculative Code Execution with Return Instructions. Paper accepted at the 31st USENIX Security Symposium, August 10–12, 2022, at the Boston Marriott Copley Place in Boston, MA, USA.

Wikner’s and Razavi’s will present their findings at the USENIX Security '22 on 12 August 2022, 1.30 pm-2.30 pm.

