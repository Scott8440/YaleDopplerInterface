
var firstCount = 2;
var secondCount = 4;
var thirdCount = 4;
var dopList1Count = 4;
var dopList2Count = 2;
var submitISS = document.getElementById("submitISS");

var growList = function(name, parent)
{
  switch(parent) {
    case 'firstList':
      var id = "firstListSelect1";
      var idBase = "firstListSelect";
      var count = firstCount;
      firstCount++;
      break;
    case 'secondList':
      var id = "secondListSelect3";
      var idBase = "secondListSelect"
      var count = secondCount;
      secondCount++;
      break;
    case 'thirdList':
      var id = "thirdListSelect1";
      var idBase = "thirdListSelect"
      var count = thirdCount;
      thirdCount++;
      break;
    case 'dopList1':
      var id = "dopList1Select3";
      var idBase = "dopList1Select"
      var count = dopList1Count;
      dopList1Count++;
      break;
    case 'dopList2':
      var id = "dopList2Select1";
      var idBase = "dopList2Select"
      var count = dopList2Count;
      dopList2Count++;
      break;
  }
  var node = document.createElement("LI");
  node.innerHTML = name+" "+count+": ";
  newSelect = node.appendChild(document.createElement("SELECT"));
  newSelect.id = idBase + count.toString();
  document.getElementById(parent).appendChild(node);
  $('#'+id+' option').clone().appendTo('#'+newSelect.id);
}

var shrinkList = function(list)
{
  var type = 0;
  if (list == 'firstList' && firstCount > 2) {
    firstCount--;
    type = 1;
  }
  else if (list == 'secondList' && secondCount > 4) {
    secondCount--;
    type = 2;
  }
  else if (list == 'thirdList' && thirdCount > 4) {
    thirdCount--;
    type = 3;
  }
  else if (list == 'dopList1' && dopList1Count > 4) {
    dopList1Count--;
    type = 4;
  }
  else if (list == 'dopList2' && dopList2Count > 2) {
    dopList2Count--;
    type = 5;
  }
  if (type != 0) {
    list = document.getElementById(list);
    item = list.lastElementChild;
    list.removeChild(item);
  }
}

var submitISSFunct = function()
{
  //Loop through form1
  //Must be at least 1
  var list1 = document.getElementById("firstList");
  var list1num = 0;
  var list1Items = list1.getElementsByTagName("input");
  for (var i = 0; i < list1Items.length; ++i) {
    if (list1Items[i].value.length > 0) {
      list1num++;
    }
  }
  //Loop through form2
  //Optional, 0 or 3+
  var list2 = document.getElementById("secondList");
  var list2num = 0;
  var list2Items = list2.getElementsByTagName("input");
  for (var i = 0; i < list2Items.length; ++i) {
    if (list2Items[i].value.length > 0) {
      list2num++;
    }
  }
  //Loop through form3
  //at least 3
  var list3 = document.getElementById("thirdList");
  var list3num = 0;
  var list3Items = list3.getElementsByTagName("input");
  for (var i = 0; i < list3Items.length; ++i) {
    if (list3Items[i].value.length > 0) {
      list3num++;
    }
  }
  //Loop through form4
  //Optional, exactly 3
  var list4 = document.getElementById("fourthList");
  var list4num = 0;
  var list4Items = list4.getElementsByTagName("input");
  for (var i = 0; i < list4Items.length; ++i) {
    if (list4Items[i].value.length > 0) {
      list4num++;
    }
  }
  if (list1num >= 1 && (list2num == 0 || list2num >= 3) && list3num >= 3 && (list4num == 3 || list4num == 0)) {
    console.log("Good input numbers");
  }

}


/*calling proc1Driver.php*/
$(document).ready(function(){
  $('#proc1Submit').click(function(){

    var emailValue  = validateEmail($('#emailField').val());
    var pID = document.getElementById('propIDp').getAttribute('value');
    var tag = pIDtoTag(pID);
    dataArr = getSelectValues();
    //Data values:
    var firstFiles = dataArr[0];
    var secondFiles = dataArr[1];
    var thirdFiles = [];
    thirdFiles.push(dataArr[2][0]);
    thirdFiles.push(dataArr[3][0]);
    thirdFiles.push(dataArr[4][0]);
    //-----------------
    var dop1Files = dataArr[5];
    var dop2Files = dataArr[6];
    var oldDSST = document.getElementById('alreadyDSSTbox').checked;

    //Call php function
    var ajaxurl = 'php\\proc1Driver.php'
    data = {'email': emailValue, 'file1arr': firstFiles,
            'file2arr': secondFiles, 'file3arr':thirdFiles,
            'dop1arr': dop1Files, 'dop2arr': dop2Files, 'tag': tag,
            'oldDSST' : oldDSST};
    console.log("before");
    $.post(ajaxurl, data, function(response) {
      console.log(response);
    });
    console.log("after");
  });
});

function populateSelect(count, listName, selectName)
{
  var Ul = document.getElementById(listName);
  var Files = Ul.getElementsByTagName("LI");
  for (var i = 1, arr = []; i < count; i++) {
    select = $('#'+selectName+i.toString()).val();
    arr.push(select);
  }
  return(arr);
}

function validateInput()
{
  propID = document.forms["processType"]["propID"].value;
  pIDlist = ['CPS', '37', '35', '76', 'CHIRPS', '33', '53', '56', '38', '42',
             '57', '55', '54', '68', '69', '70', '61', '44', '52', '59', '46',
             '63', '62', '58', '64', '66', '65', '71', '0', '67', '60', '72',
             '74', '78', '80', '75', '81', '79', '73', '77', '82', '87', '91',
             '99', '104', '84', '88', '83', '100', '105', '103', '85', '86',
             '106', '93', '94', '89', '101', '90', '96', '102', '97', '98',
             '115', '124', '125', '132', '109', '122', '117', '144', '111',
             '114', '139', '108', '143', '145', '147', '112', '113', '140',
             '116', '152', '153', '151', '123', '133', '141', '135', '142',
             '126', '137', '138', '128', '164', '131', '170', '154', '165',
             '182', '157', '162', '166', '188', '160', '161', '186', '158',
             '178', '187', '180', '181', '183', '184', '171', '174', '192',
             '191', '190', '136', '185', '175', '189', '193', '173', '194',
             '176', '163', '159', '167', '172', '195', '177', '179', '196',
             '155', '209', '200', '208', '206', '211', '210', '199', '197',
             '198', '207', '203', '218', '201', '217', '220', '215', '219',
             '221', '202', '222', '205', '213', '216', '212', '223', '224',
             '225', '204', '226', '227', '228', '243', '241', '235', '240',
             '248', '233', '229', '236', '242', '232', '237', '247', '254',
             '234', '249', '239', '246', '250', '238', '255', '230', '256',
             '251', '244', '231', '258', '257', '252', '260', '259', '262',
             '263', '264', '265', '245', '274', '267', '266', '276', '277',
             '278', '282', '285', '284', '283', '287', '294', '273', '300',
             '292', '293', '280', '291', '304', '299', '271', '296', '272',
             '289', '305', '303', '301', '281', '279', '298', '308', '309',
             '295', '311', '307', '312', '306', '269', '302', '297', '314',
             '316', '315', '317', '318', '310', '288', '322', '321', '320',
             '319', '323', '324', '325', '290', '326', '327', '329', '330',
             '331', '332', '341', '313', '344', '345', '343', '336', '334',
             '347', '349', 'cal', '275', 'test', '339', '335', '342', '348',
             '346', '350', '352', '340', '337', '351', '356', '357', '359',
             '358', '360', '362', '150', '30', '353', '368', '367', '366',
             '365', '380', '377', '376', '375', '372', '378', '373', '374',
             '369', '379', '371', '370', '381', '384', '385', '382', '386',
             '387', '390', '388']
  var found = $.inArray(propID, pIDlist) > -1;
  if (!found) {
    document.getElementById('processType').action='';
    badString = 'Not a valid proposal ID'
    alert(badString);
    return false;
  }
}

function Create2DArray(rows)
{
  var arr = [];

  for (var i=0;i<rows;i++) {
     arr[i] = [];
  }
  return arr;
}

//select is an HTML select element
function getSelectValues()
{
  var selectArr = [7]
  selectArr[0] = document.getElementById('firstListSelect1');
  selectArr[1] = document.getElementById('secondListSelect1');
  selectArr[2] = document.getElementById('thirdListSelect1');
  selectArr[3] = document.getElementById('thirdListSelect2');
  selectArr[4] = document.getElementById('thirdListSelect3');
  selectArr[5] = document.getElementById('dopList1Select1');
  selectArr[6] = document.getElementById('dopList2Select1');

  var resultArr = Create2DArray(7);

  for (i = 0; i < 7; i++) {
    var options = selectArr[i] && selectArr[i].options;
    var opt;

    for (var j=0, iLen=options.length; j<iLen; j++) {
      opt = options[j];

      if (opt.selected) {
        resultArr[i].push(opt.value || opt.text);
      }
    }
  }
  return resultArr;
}

function displaySelect(element)
{
  select = element.getElementsByTagName("SELECT")[0];
  var resultArr = [];
  var options = select && select.options;
  var opt;

  for (var j = 0, iLen=options.length; j<iLen; j++) {
    opt = options[j];

    if (opt.selected) {
      resultArr.push(opt.value || opt.text);
    }
  }
  var string = ""
  if (resultArr.length == 0) {
    string = "";
  }
  else {
    string = "Selected Observations: ";
    for (var i = 0, len=resultArr.length; i<len; i++) {
      string += (resultArr[i] + " ");
    }
  }
  element.getElementsByTagName("P")[0].innerHTML = string;
}

function checkAndDisplay(element)
{
  select = element.getElementsByTagName("SELECT")[0];
  var resultArr = [];
  var options = select && select.options;
  var opt;

  for (var j = 0, iLen=options.length; j<iLen; j++) {
    opt = options[j];

    if (opt.selected) {
      resultArr.push(opt.value || opt.text);
    }
  }
  dateArr = [];
  for (var i = 0; i < resultArr.length; i++) {
    var date = resultArr[i].split("");
    date = date.slice(0,6);
    date = date.join("");
    dateArr.push(date);
  }
  //Check if all of the dates are the same
  var first = dateArr[0];
  dissimilar = false;
  for (var i = 0; i < dateArr.length; i++) {
    if (dateArr[i] != first) {
      dissimilar = true;
      break;
    }
  }
  if (!dissimilar) {                      //Dates are the same
    //Check if observation numbers are consecutive
    numArr = [];
    var nonconsecutive = false;
    for (var i = 0; i < resultArr.length; i++) {
      var num = resultArr[i].split("");
      num = num.slice(7,11);
      num = num.join("");
      numArr.push(num);
    }
    for (var i = 0; i < numArr.length - 1; i++) {
      current = numArr[i];
      if (current != (numArr[i+1] - 1)) {
        nonconsecutive = true;
      }
    }
    if (!nonconsecutive) {
      var string = ""
      if (resultArr.length == 0) {
        string = "";
      }
      else {
        string = "Selected Observations: ";
        for (var i = 0, len=resultArr.length; i<len; i++) {
          string += (resultArr[i] + " ");
        }
      }
      element.getElementsByTagName("P")[0].innerHTML = string;

    }
    else {
      var badString = "* WARNING: Observations must be consecutive"
      badString = badString.fontcolor("red");
      element.getElementsByTagName("P")[0].innerHTML = badString;
    }
  }
  else {
    var badString = "* WARNING: Observations must be from the same night";
    badString = badString.fontcolor("red")
    element.getElementsByTagName("P")[0].innerHTML = badString;
  }
}

function validateEmail(email)
{
  email = email
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");

  var re = /\S+@\S+\.\S+/;

  if (re.test(email)) {
    console.log("Good");
    return email;
  }
  else {
    console.log("Bad");
    //Do something else
  }

}

function pIDtoTag(pid)
{
  pid = pid.concat('i');
  return pid
}

function alreadyDSST(star)
{
  madeDSSTs = ['4628', 'HD82074', '10700', '11909', '11964A', '20794', '22049',
               '32147', '43834', '72673', '90125', '94683', '100623', '115404',
               '131156A', '131156B', '136442', '149661', '156274',
               '165341A', '172051', '177565', '188088', '191408A', '194215',
               '196761', '208801', '209100', '211998']
  var found = $.inArray(star, madeDSSTs) > -1;
  if (found) {
    document.getElementById('alreadyDSSTalert').innerHTML = 'A DSST already exists for this star. Check \
    the box box if you want to use this DSST. Otherwise continue entering observations.';
    document.getElementById('alreadyDSSTalert').style.display = 'inline';
    document.getElementById("alreadyDSSTbox").style.display = "inline";
  }
}

$(document).ready(function(){
  $('#alreadyDSSTbox').click(function(){
    var val = document.getElementById('alreadyDSSTbox').checked;
    $('.iss').toggle();
  });
});
