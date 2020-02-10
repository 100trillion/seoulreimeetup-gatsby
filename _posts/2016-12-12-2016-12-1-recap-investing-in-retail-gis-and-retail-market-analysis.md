---
id: 9
title: 'Recap: “Investing in Retail &#8211; GIS and Retail Market Analysis”'
date: 2016-12-12T03:47:21+00:00
author: jlbleese
excerpt: '<p>On November 17, the Seoul Real Estate Investing Meetup invited <a target="_blank" href="https://kr.linkedin.com/in/rjchetti" rel="noopener noreferrer">Raymond Chetti</a>, an Urban Planner and Retail Market Analyst, to give a presentation entitled “Investing in Retail - GIS and Retail Market Analysis.”</p><p>The event was attended by approximately 75 community members and held at <a target="_blank" href="https://www.wework.com/buildings/gangnam-station--seoul" rel="noopener noreferrer">WeWork Gangnam Station</a>, who sponsored the event by providing free craft beer and event space. <a target="_blank" href="https://kr.linkedin.com/in/martin-bax-936b33115" rel="noopener noreferrer">Martin Bax</a>, a professional interpreter, provided simultaneous English-to-Korean interpretation via a headset.</p>'
layout: post
guid: http://localhost:8888/seoulreimeetup/2016/12/12/2016-12-1-recap-investing-in-retail-gis-and-retail-market-analysis/
permalink: /2016/12/12/2016-12-1-recap-investing-in-retail-gis-and-retail-market-analysis/
categories:
  - GIS
  - Korea
  - real estate
  - retail
  - Seoul
tags:
  - ArcGIS
  - demographics
  - Esri Story Maps
  - IFC Mall
  - KOSIS
  - KTDB
  - Raymond Chetti
  - SGIS
  - Starfield Hanam
---
<span style="font-size:16px">On November 17, the Seoul Real Estate Investing Meetup invited <a target="_blank" href="https://kr.linkedin.com/in/rjchetti" rel="noopener noreferrer">Raymond Chetti</a>, a</span><span style="font-size:16px">n Urban Planner and Retail Market Analyst, to give a presentation entitled “Investing in Retail &#8211; GIS and Retail Market Analysis.”</span>

<span style="font-size:16px">The event was attended by approximately 75 community members and held at </span><a target="_blank" href="https://www.wework.com/buildings/gangnam-station--seoul" rel="noopener noreferrer"><span style="font-size:16px">WeWork Gangnam Station</span></a><span style="font-size:16px">, who sponsored the event by providing free craft beer and event space. <a target="_blank" href="https://kr.linkedin.com/in/martin-bax-936b33115" rel="noopener noreferrer">Martin Bax</a>, a professional interpreter, provided simultaneous English-to-Korean interpretation via a headset.</span>

  
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-9622762641247774"
     data-ad-slot="6851776325"></ins>  


## The Huff Model

<span style="font-size:16px">In his presentation, Raymond used an adaptation of the </span><a target="_blank" href="http://www.directionsmag.com/entry/retail-trade-area-analysis-using-the-huff-model/123411" rel="noopener noreferrer"><span style="font-size:16px">Huff Model</span></a> <span style="font-size:16px">to determine the sales potential of a hypothetical coffee shop investment in Mangwon-dong, Mapo-gu. The basic premise of the model is that the closer to a person&#8217;s residence and the more attractive a retail development is,&nbsp;the higher the likelihood that he or she will visit that place.</span><figure style="width: 2054px" class="wp-caption alignnone">

![ Raymond showing members of the Seoul Real Estate Investing Meetup the distance between Dongdaemun-gu and IFC Mall in Yeouido.&nbsp;(Photo by Cristian Bucur) ](https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1481385669690-FLYCYW05FO2RH07K7BOH/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/raymond?format=original) <figcaption class="wp-caption-text">Raymond showing members of the Seoul Real Estate Investing Meetup the distance between Dongdaemun-gu and IFC Mall in Yeouido.&nbsp;(Photo by Cristian Bucur)</figcaption></figure> 

<span style="font-size:16px">Raymond began by illustrating how the Huff Model works by comparing the distance and attractiveness of two retail mall developments&#8211;IFC Mall and Shinsegae Starfield Hanam&#8211;for a Dongdaemun-gu resident.</span>

<span style="font-size:16px">One method of calculating the distance between two points is to draw a straight line between the two, disregarding geographical features (e.g., the Han river) and the transportation network. The second method is to account for the transportation network, he said.</span>

<span style="font-size:16px">Using the latter method, Raymond determined that IFC Mall is 27 minutes away by car for Dongdaemun-gu residents while Starfield Hanam is just an extra 10 minutes away.</span>

<span style="font-size:16px">However, given that Starfield Hanam is four times larger than IFC Mall, Dongdaemun-gu residents are more likely to shop at Starfield Hanam despite it being further away. He noted that where shopping malls are concerned, size is often a determining factor of attractiveness.</span>

## Supply, demand, and transportation

<span style="font-size:16px">In the next part of his presentation, Raymond demonstrated how he uses </span><a target="_blank" href="https://www.arcgis.com/features/index.html" rel="noopener noreferrer"><span style="font-size:16px">ArcGIS</span></a> <span style="font-size:16px">to gather data and implement a comprehensive retail market analysis. </span>

<span style="font-size:16px">He looked at several factors including supply, demand, and Seoul’s transportation network. A number of data sources including the </span><a target="_blank" href="http://kosis.kr/" rel="noopener noreferrer"><span style="font-size:16px">KOSIS</span></a> <span style="font-size:16px">(Korean Statistical Information Service), </span><a target="_blank" href="https://sgis.kostat.go.kr/view/index" rel="noopener noreferrer"><span style="font-size:16px">SGIS</span></a><span style="font-size:16px">, the </span><a target="_blank" href="https://www.ktdb.go.kr/" rel="noopener noreferrer"><span style="font-size:16px">KTDB</span></a> <span style="font-size:16px">(Korea Transport Database), and other undisclosed sources were used to inform his analysis. As a GIS consultant, “you have to find all the data and put the pieces of the puzzle together. . . . You need to always be looking for data,” he said.</span>

<span style="font-size:16px">Supply was determined by the number of competitive coffee shops within a one-kilometer radius of the proposed café site. These were visualized on an interactive map with </span><a target="_blank" href="http://support.esri.com/other-resources/gis-dictionary/term/point%20feature" rel="noopener noreferrer"><span style="font-size:16px">point features</span></a><span style="font-size:16px">. Raymond found 173 cafés and, for the sake of illustration, assumed an attractiveness score of 100 for all coffee shops. Selecting a supply point would display the coffee shop’s name, address, and probability of sales.</span>

<span style="font-size:16px">Demand was calculated by importing census data from the KOSIS into ArcGIS to create interactive </span><a target="_blank" href="http://support.esri.com/sitecore/content/support/Home/other-resources/gis-dictionary/term/graduated%20color%20map" rel="noopener noreferrer"><span style="font-size:16px">graduated color maps</span></a><span style="font-size:16px">. This included both macro and micro data about population, number of households, household growth, average income, and spending per household. To get a more accurate picture of the population distribution within individual neighborhoods, population density map images from SGIS were </span><a target="_blank" href="http://support.esri.com/other-resources/gis-dictionary/term/georeferencing" rel="noopener noreferrer"><span style="font-size:16px">georeferenced</span></a> <span style="font-size:16px">in ArcGIS.</span>

<span style="font-size:16px">Spending on coffee and tea was calculated by taking an aggregate of spending per household multiplied by the number of households in the coffee shop’s catchment area.</span><figure style="width: 2054px" class="wp-caption alignnone">

![ Raymond referring to a graduated color map in ArcGIS showing total coffee and tea sales by district for 2015. The darker areas represent districts with high coffee and tea sales.&nbsp;(Photo by Cristian Bucur) ](https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1481385779089-DRQYX1GYLQ55Q2AR6YLA/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/raymond?format=original) <figcaption class="wp-caption-text">Raymond referring to a graduated color map in ArcGIS showing total coffee and tea sales by district for 2015. The darker areas represent districts with high coffee and tea sales.&nbsp;(Photo by Cristian Bucur)</figcaption></figure> 

<span style="font-size:16px">Raymond’s analysis of the transportation network took into account both the road and metro system, for which information was sourced from the KTDB. This included the maximum speed of all subway lines and major roads in the city. </span><span style="font-size:16px">Raymond assumed that roads not indexed on the KTDB are smaller roads with maximum speed limits of 15 or 25 kilometers per hour.</span>

<span style="font-size:16px"><a target="_blank" href="http://www.businesskorea.co.kr/english/news/politics/11295-subway-extension-english-language-map-released-seouls-10-planned-subway-lines" rel="noopener noreferrer">Newly planned subway lines and extensions</a>&nbsp;were also included in the analysis.</span>

<span style="font-size:16px">Once Raymond had collected all of the necessary data about supply, demand, and the transportation network, he used the </span><a target="_blank" href="http://desktop.arcgis.com/en/arcmap/10.3/manage-data/creating-new-features/merging-features-in-the-same-layer.htm" rel="noopener noreferrer"><span style="font-size:16px">merge</span></a> <span style="font-size:16px">tool in ArcGIS to combine these datasets into a single dataset. He was then able to calculate the probability of sales for the coffee shop in question.</span>

<span style="font-size:16px">Raymond concluded his presentation by showing investors how <a target="_blank" href="https://storymaps.arcgis.com/en/" rel="noopener noreferrer">Esri Story Maps</a> may be used to pitch such retails investments to potential investors in a visually attractive way.</span>

<span style="font-size:16px">If you are interested in working with Raymond Chetti, please email him at </span><span style="font-size:16px">raychetti@gmail.com</span><span style="font-size:16px">.</span>

<div class="image-gallery-wrapper">
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588339119-D9PR3PV7EI40G6UC1WRA/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-9.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588339118-2PVIFIQTXWW4LLVVTMN4/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-29.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588340139-A2B4IN2YQXE7MQFLXBTH/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-32.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588340459-ETST3KCUL3T5W5LW74B9/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-33.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588342209-R2DP7I22ATMN3YMC4B7H/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-57.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588342542-V54VU3PCJ76MRF4NQQUE/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-73.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1519141697426-BVEK2P98GOX6YGB6NOO7/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-50.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1519141725360-J5VZG4GJSESQ8EAXJS6M/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-66.jpg?format=original" />
  </p>
  
  <p>
    <img src="https://images.squarespace-cdn.com/content/v1/568a65ced82d5eb432851580/1480588343324-QY5ULJQID322DJYVGZ7Y/ke17ZwdGBToddI8pDm48kP75_OXatt7PDh77yUpp9qV7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1Uaj_r05lA3kBpZp5o3VQTrN4WsXwHNhl_XIcvoFTFHOWJilkUu7eIyBb-AQDEk_nZw/TSREI-83.jpg?format=original" />
  </p>
</div>

## More about the Seoul Real Estate Investing Meetup

<span style="font-size:16px">Raymond is just the latest speaker in a series of speakers that the Seoul Real Estate Investing Meetup has invited to speak. Some of our past speakers have included:</span>

  * <a target="_blank" href="https://www.linkedin.com/in/nikola-medimorec-b0b72030" rel="noopener noreferrer"><span style="font-size:16px">Nikola Medimorec</span></a> <span style="font-size:16px">&#8211; a sustainable transport expert at t</span><span style="font-size:16px">he Partnership on Sustainable, Low Carbon Transport (SLoCaT)&nbsp;</span><span style="font-size:16px">and Co-Author of </span><a target="_blank" href="http://kojects.com/" rel="noopener noreferrer"><span style="font-size:16px">Kojects</span></a><span style="font-size:16px">, a blog about the various construction and urban development projects around Seoul and the rest of South Korea</span>
  * <span style="font-size:16px"><a target="_blank" href="https://www.facebook.com/sangtaek.jeong?ref=br_rs" rel="noopener noreferrer"><span style="font-size:16px">Jeong Sangtaek</span></a><span style="font-size:16px"> &#8211; Director of the Small Business Development Division at </span><a target="_blank" href="http://www.seoul.go.kr/" rel="noopener noreferrer"><span style="font-size:16px">Seoul Metropolitan Government</span></a></span>
  * <a target="_blank" href="https://www.linkedin.com/in/steve-seongtae-nam-26051133?authType=NAME_SEARCH&authToken=uiJn&locale=en_US&srchid=1946947401481384624459&srchindex=1&srchtotal=1&trk=vsrp_people_res_name&trkInfo=VSRPsearchId%3A1946947401481384624459%2CVSRPtargetId%3A117720360%2CVSRPcmpt%3Aprimary%2CVSRPnm%3Atrue%2CauthType%3ANAME_SEARCH" rel="noopener noreferrer"><span style="font-size:16px">Nam Seongtae</span></a> <span style="font-size:16px">&#8211; Former Investment Consultant at </span><a target="_blank" href="http://www.cushmanwakefield.com/" rel="noopener noreferrer"><span style="font-size:16px">Cushman & Wakefield</span></a> <span style="font-size:16px">and current CEO of </span><a target="_blank" href="https://zipadvisor.co/" rel="noopener noreferrer"><span style="font-size:16px">ZipAdvisor</span></a><span style="font-size:16px">,&nbsp;a tech-based d</span><span style="font-size:16px">ata, valuation, and analytics tool.</span>

<span style="font-size:16px">The Seoul Real Estate Investing Meetup is one of the largest real estate and business-related networks in Korea. Its main goal is to provide continuing education and networking opportunities to its members and to help them make smarter investment decisions and advance their real estate goals.</span>

<span style="font-size:16px">If you are interested in sponsoring an event, being a speaker, or presenting an investment opportunity to our members, please get in touch.</span>

_<span style="font-size:16px">(Banner photo by Cristian Bucur)</span>_