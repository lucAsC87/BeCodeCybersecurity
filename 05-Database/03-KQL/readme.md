
# KQL

## Where does the name Kusto come from? (from Kusto Query Language)

*So, KQL is named after Jacques Cousteau. Even today, you can find evidence of this in our own Azure Monitor Docs. If you go to the [datatable operator](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/datatableoperator?pivots=azuredataexplorer) page right now, you’ll still find a reference to Mr. Cousteau in an example that lists his date of birth, the date he entered the naval academy, when he published his first book entitled “The Silent World: A Story of Undersea Discovery and Adventure,” and the date of his passing.*

*So, I hope you’re catching on to this. If not, what is it that we are trying to accomplish when we query data tables for security purposes? What is it that we’re trying to accomplish though Hunting exercises and operations?* 

*The answer?* 

*We are exploring the depths of our data. We are attempting to surface the critical and necessary security information that will tell us about potential exposure through simple, powerful queries.*

### A Common KQL Workflow

![](/assets/kql.png/)

Let’s break this query down by the steps. 

1. The first step is to identify the table we want to query against. This table will contain the information that we’re looking for. In our example here, we’re querying the SecurityEvent table. The SecurityEvent table contains security events collected from windows machines by Microsoft Defender for Cloud or Microsoft Sentinel. For a full list of all services tables, see the Azure [ Monitor Logs table reference ](https://docs.microsoft.com/en-us/azure/azure-monitor/reference/tables/tables-category) .

2. The pipe (|) character (the shifted key above the Enter key on most keyboards) is used to separate commands issued to the query engine. You can see here that each command is on its own line. It doesn’t have to be this way. A KQL query can actually be all one single line. For our efforts, and as a recommendation, I prefer each command on its own line. For me, it’s just neater and more organized which makes it easier to troubleshoot when a query fails or when I need to adjust the query to produce different results. 

3. Next, we want to filter the data in some way. If I simply entered the table and ran that as its own, single query, it would run just fine. Doing that returns all rows and columns (up to a limit – which I believe is now 50,000 rows) of the data stored in the table. But our goal is getting exact data back. As an analyst looking for threats, we don’t want to have to sift through 50,000 rows of data. No, we want to look for specific things. The** Where operator** is one of the best ways to accomplish this. You can see here in the example that I’m filtering first by when the occurrence happened (TimeGenerated) and then (remember the pipe character – another line, another command) by a common Windows Event ID (4624 – successful login). 

4. The next step in our workflow is to provide data aggregation. What do we want to do with this filtered data? In our case in the example, we want to create a count of the Accounts (usernames) that produced a successful login (EventID 4624) in the last 1 hour (TimeGenerated). 

5. Next let’s tell the query engine how we want to order the results. Using the Order operator, I’m telling the query engine that when the results are displayed, I want it shown in alphabetical order by the Account column. The ‘asc’ in the query in the Order Data step is what produces this ordering. If we wanted descending order, we’d use ‘desc’. Don’t worry, we’ll dig deeper into each of these operators as we go along in the series. 

6. Generally, the last thing that I’ll do with this search query is tell the query engine exactly what data I want displayed. The [Project operator](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/projectoperator)  is a powerful command. We’ll dig deeper into this operator later in this series, but for our step here, I’m telling the query engine that after all my filtering, data aggregation, and ordering, I only want to display two columns in my results: Account and SuccessfulLogins.

7. Our search query output is exactly that:                

![](/assets/kql_query_windows.png)


See that? The Account column is in alphabetical order ascending and the SuccessfulLogons column shows how many times each Account successfully logged in. 

If you need to, jump back through each step above until you get a good understanding of the workflow. Again, this is very common, and you’ll see this structure many times working with Microsoft Sentinel and Defender products. Remember, it’s about the results. If you can look at this example and get a good feeling that you understand how the results were accomplished, line-by-line, you’re on your way. 

I invite you, though, to take this example and copy/paste it into a Logs environment to test. You can have this query to play with it in your own Microsoft Sentinel environment or using the KQL Playground I provided as a resource in Part 1.

```sql
SecurityEvent 
| where TimeGenerated > ago (1h)  
| where EventID == 4624 
| summarize count() by Account 
| order by Account asc 
| project Account , SuccessfulLogons = count_ 
```


This query is also available from the GitHub repository for this blog series: https://aka.ms/MustLearnKQL 

I’d like to share one extra tidbit with you that you might find helpful as you start testing this KQL query example in your own, or our, environment. Every language (scripting, coding, querying) has the capability to add comments or comment-out code through special characters. When the query, scripting, or development engine locates these characters, it just skips them. KQL has this same type of character. The character for KQL is the double forwardslash, or //

When you start testing this post’s KQL query example, comment-out a line or two (put the double forwardslash at the beginning of the line) and rerun the query just to see how eliminating a single line can alter the results. You’ll find that this is an important technique as you start developing your own KQL queries. I’ll talk about this more later, too. 

In the next post (Part 4) I’ll talk through another, yet just as powerful, way to search for information using KQL that is a top pocket tool for Threat Hunters. 

And, then I’ll come back for Part 5 and show how to tie together both search methods to create the full operation of hunting to Analytics Rule. But don’t worry, that’s not the end. I have no clue how many parts this series be. A lot of it depends on you.

**Write your first query with Kusto Query Language (Learn module)**
https://docs.microsoft.com/en-us/learn/modules/write-first-query-kusto-query-language/

**KQL Playground – only need a valid Microsoft account to access.**
https://aka.ms/LADemo


 [KQL Agent CTF](https://detective.kusto.io/) **Play to earn a MS certificate.** 


[MustLearnKQL](./MustLearnKQL_Book.pdf ) 
[KQL](https://www.youtube.com/playlist?list=PLD7rlIrZEkLgiRbIs_5JXIxzu-5tpoDbd) 


Resources : 

[Azure Monitor table reference index by category | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/tables-category)
[KQL/kql_cheat_sheet_dark.pdf at master · marcusbakker/KQL · GitHub](https://github.com/marcusbakker/KQL/blob/master/kql_cheat_sheet_dark.pdf)
[dataexplorer-docs/data-explorer/kusto/query/splunk-cheat-sheet.md at main · MicrosoftDocs/dataexplorer-docs · GitHub](https://github.com/MicrosoftDocs/dataexplorer-docs/blob/main/data-explorer/kusto/query/splunk-cheat-sheet.md)


	 
