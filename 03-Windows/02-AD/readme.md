## Windows Server AD 

- Type of Challenge: `Learning` 
- Duration: `2 days`
- Challenge Type : `solo`

## Overview

This challenge guides you through deploying a secure Windows Server 2022 environment with Active Directory, essential server roles (IIS, DNS, DHCP), user management, Sysmon monitoring, and demonstration of its functionality to a client. Gain essential configuration skills, security awareness, and experience with Active Directory while incorporating user accounts like Alice and Bob for realistic role-based access.

## Learning Objectives:

* Install and configure Windows Server 2022.
* Create and manage user accounts within Active Directory.
* Set up and configure Active Directory for centralized user management.
* Apply granular permissions for users like Alice and Bob based on security principles.
* Install and configure essential server roles (IIS, DNS, DHCP).
* Implement Sysmon for system activity monitoring.
* Analyze Sysmon data and present its security value to the client.

You can follow [this](https://openclassrooms.com/en/courses/7710301-manage-windows-server) tutorial to discover windows server.

## Environment:

**Resources:**

* Virtualization software: Microsoft Hyper-V, VMware Workstation, VirtualBox, QEMU.
* **Required:** <br>
[Windows Server 2022 evaluation](https://www.microsoft.com/evalcenter/evaluate-windows-server-2022)
* [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) monitoring solution

## Steps:

**1. System Preparation:**

1. Set up your virtualization environment with multiple VMs:
    - Server VM (Windows Server 2022 installation)
    - Client VMs (for access and monitoring)
    - Domain Controller VM (Active Directory installation)

2. Download and install Windows Server 2022 evaluation on the Server VM and Domain Controller VM.

**If you're short of resources, you can use just one server, which will be your domain controller, and one client.**

#### **Must have** : 


**2. Active Directory Setup:**

1. Promote the Domain Controller VM to a domain controller.
2. Create a new Active Directory forest and domain structure.
3. Configure DNS service on the Domain Controller VM.
4. Create organizational units (OUs) for user and group management.
5. Join the Server VM and Client VMs to the domain.

**3. User Management with Alice and Bob:**

1. Create user accounts within Active Directory:
    - Alice (Administrator, assigned to dedicated OU)
    - Bob (Standard User with access to `/Users/Bob` folder, assigned to specific OU)
2. Leverage Group Policy Objects (GPOs) to configure user settings based on OUs.
3. Implement granular permissions based on security principles for both Alice and Bob.

**4. Server Roles:**

**4.1 IIS for Alice:**

1. Install and configure [IIS](https://www.iis.net/overview) on the Server VM for Alice's specific web application/service.

2. Apply robust security best practices (permissions, WAFs, considering Alice's admin role).
3. Test the web application and ensure accessibility for authorized users in the domain.

**4.2 DNS:**

1. Verify DNS functionality within the Active Directory domain environment.
2. Configure conditional forwarders or external DNS integration if needed.

**4.3 DHCP:**

1. Install and configure DHCP on the Server VM for automatic IP assignment within the domain.

2. Integrate DHCP with Active Directory for dynamic DNS updates (optional).

#### **Cool to have** :

**5. Sysmon Monitoring:**

1. Install and configure your chosen [Sysmon monitoring](https://syedhasan010.medium.com/sysmon-how-to-setup-configure-and-analyze-the-system-monitors-events-930e9add78d) solution on the Server VM.
2. Configure Sysmon to capture relevant events and filter noise specific to your domain environment and user activities (e.g., Alice's admin actions, Bob's file access).
3. Demonstrate Sysmon functionality by simulating suspicious activities and capturing events related to both Alice and Bob.

**6. Client-Side Access and Reporting:**

1. Connect to the Server VM from the Client VMs using domain credentials (Alice and Bob).
2. Verify access based on assigned user permissions and GPOs, demonstrating differences between Alice and Bob's access levels.
3. Access and analyze Sysmon logs using your chosen solution.
4. Prepare a client-facing report highlighting captured events, potential security concerns related to both Alice and Bob, and Sysmon's value within the Active Directory domain.

**Evaluation:**

- Successful completion of all steps (Active Directory setup, user management, roles, Sysmon implementation).
- Demonstration of Sysmon functionality and client-facing report generation, covering both Alice and Bob's scenarios.
- Understanding and application of security best practices throughout the configuration, considering user roles and permissions.

**Additional Notes:**

- Explore beyond basic steps and experiment with different configurations for learning.
- Prioritize security best practices throughout the setup, especially within Active Directory and user account management.


