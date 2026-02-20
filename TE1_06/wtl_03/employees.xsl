<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>
<head>
    <title>Employee Details</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            font-family: Arial;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>
<h2>Employee Information Table</h2>

<table>
<tr>
    <th>Employee ID</th>
    <th>Name</th>
    <th>Position</th>
    <th>Organization</th>
    <th>Department</th>
    <th>Salary</th>
</tr>

<xsl:for-each select="employees/employee">
<tr>
    <td><xsl:value-of select="emp_id"/></td>
    <td><xsl:value-of select="name"/></td>
    <td><xsl:value-of select="position"/></td>
    <td><xsl:value-of select="organization"/></td>
    <td><xsl:value-of select="department"/></td>
    <td><xsl:value-of select="salary"/></td>
</tr>
</xsl:for-each>

</table>
</body>
</html>

</xsl:template>
</xsl:stylesheet>
