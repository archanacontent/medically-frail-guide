<?xml version="1.0" encoding="UTF-8"?>
<!-- Azure Blue print styling for the DITA-OT PDF2 output -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" version="2.0">
  <xsl:variable name="page-width">210mm</xsl:variable>
  <xsl:variable name="page-height">297mm</xsl:variable>
  <xsl:variable name="default-font-size">10pt</xsl:variable>
  <xsl:variable name="side-col-width">0pt</xsl:variable>

  <xsl:attribute-set name="__fo__root" use-attribute-sets="base-font">
    <xsl:attribute name="font-family">sans-serif</xsl:attribute>
    <xsl:attribute name="color">#26394d</xsl:attribute>
    <xsl:attribute name="line-height">1.45</xsl:attribute>
    <xsl:attribute name="xml:lang" select="translate($locale, '_', '-')"/>
    <xsl:attribute name="writing-mode" select="$writing-mode"/>
  </xsl:attribute-set>

  <xsl:attribute-set name="common.link">
    <xsl:attribute name="color">#0078d4</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="color">#005a9e</xsl:attribute>
    <xsl:attribute name="font-size">20pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="border-after-style">solid</xsl:attribute>
    <xsl:attribute name="border-after-width">2pt</xsl:attribute>
    <xsl:attribute name="border-after-color">#0078d4</xsl:attribute>
    <xsl:attribute name="space-before">0pt</xsl:attribute>
    <xsl:attribute name="space-after">14pt</xsl:attribute>
    <xsl:attribute name="padding-after">6pt</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="topic.topic.title" use-attribute-sets="common.title">
    <xsl:attribute name="color">#0f2236</xsl:attribute>
    <xsl:attribute name="font-size">13pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="space-before">14pt</xsl:attribute>
    <xsl:attribute name="space-after">4pt</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="section.title" use-attribute-sets="common.title">
    <xsl:attribute name="color">#005a9e</xsl:attribute>
    <xsl:attribute name="font-size">12pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="space-before">14pt</xsl:attribute>
    <xsl:attribute name="space-after">4pt</xsl:attribute>
    <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="shortdesc">
    <xsl:attribute name="font-size">11.5pt</xsl:attribute>
    <xsl:attribute name="color">#0f2236</xsl:attribute>
    <xsl:attribute name="space-after">10pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="image">
    <xsl:attribute name="content-width">105mm</xsl:attribute>
    <xsl:attribute name="scaling">uniform</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="fig">
    <xsl:attribute name="space-before">10pt</xsl:attribute>
    <xsl:attribute name="space-after">12pt</xsl:attribute>
    <xsl:attribute name="keep-together.within-page">always</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="fig.title" use-attribute-sets="common.title">
    <xsl:attribute name="font-size">8.5pt</xsl:attribute>
    <xsl:attribute name="color">#5a6f84</xsl:attribute>
    <xsl:attribute name="font-weight">normal</xsl:attribute>
    <xsl:attribute name="space-before">4pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="dlentry.dt__content">
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#0f2236</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="note__table">
    <xsl:attribute name="space-before">8pt</xsl:attribute>
    <xsl:attribute name="space-after">8pt</xsl:attribute>
    <xsl:attribute name="background-color">#eef5fc</xsl:attribute>
    <xsl:attribute name="padding">6pt</xsl:attribute>
  </xsl:attribute-set>

  <xsl:attribute-set name="__frontmatter__title" use-attribute-sets="common.title">
    <xsl:attribute name="space-before">70mm</xsl:attribute>
    <xsl:attribute name="space-before.conditionality">retain</xsl:attribute>
    <xsl:attribute name="font-size">26pt</xsl:attribute>
    <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="line-height">1.2</xsl:attribute>
    <xsl:attribute name="color">#005a9e</xsl:attribute>
    <xsl:attribute name="text-align">start</xsl:attribute>
  </xsl:attribute-set>
</xsl:stylesheet>
