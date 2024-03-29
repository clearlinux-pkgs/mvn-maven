#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven
Version  : 2.2.0
Release  : 8
URL      : https://github.com/apache/maven/archive/maven-2.2.0.tar.gz
Source0  : https://github.com/apache/maven/archive/maven-2.2.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.1/maven-2.0.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.10/maven-2.0.10.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.11/maven-2.0.11.pom
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.2/maven-2.0.2.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.4/maven-2.0.4.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.5/maven-2.0.5.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.6/maven-2.0.6.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.7/maven-2.0.7.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.8/maven-2.0.8.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0.9/maven-2.0.9.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.0/maven-2.0.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.1.0/maven-2.1.0.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.2.0/maven-2.2.0.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/maven/2.2.1/maven-2.2.1.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.0.3/maven-3.0.3.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.0.4/maven-3.0.4.pom
Source17  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.0.5/maven-3.0.5.pom
Source18  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.0/maven-3.0.pom
Source19  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.3.9/maven-3.3.9.pom
Source20  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.6.1/maven-3.6.1.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/maven/3.6.1/maven-3.6.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-data = %{version}-%{release}
Requires: mvn-maven-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
-------------------------------------------------------------------------------
Bootstrapping Maven
-------------------------------------------------------------------------------

%package data
Summary: data components for the mvn-maven package.
Group: Data

%description data
data components for the mvn-maven package.


%package license
Summary: license components for the mvn-maven package.
Group: Default

%description license
license components for the mvn-maven package.


%prep
%setup -q -n maven-maven-2.2.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven
cp apache-maven/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-maven/apache-maven_LICENSE.txt
cp maven-core/checkstyle-license.txt %{buildroot}/usr/share/package-licenses/mvn-maven/maven-core_checkstyle-license.txt
cp maven-model/src/test/java/org/apache/maven/model/LicenseTest.java %{buildroot}/usr/share/package-licenses/mvn-maven/maven-model_src_test_java_org_apache_maven_model_LicenseTest.java
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.1/maven-2.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.10/maven-2.0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.11
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.11/maven-2.0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.2/maven-2.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.4/maven-2.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.5
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.5/maven-2.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.6
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.6/maven-2.0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.7
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.7/maven-2.0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.8
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.8/maven-2.0.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.9
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.9/maven-2.0.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.0/maven-2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.1.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.1.0/maven-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.0/maven-2.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.1
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.1/maven-2.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.3
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.3/maven-3.0.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.4
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.4/maven-3.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.5
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.5/maven-3.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.0/maven-3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.3.9
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.3.9/maven-3.3.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.6.1
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.6.1/maven-3.6.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.6.1
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven/3.6.1/maven-3.6.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.1/maven-2.0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.10/maven-2.0.10.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.11/maven-2.0.11.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.2/maven-2.0.2.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.4/maven-2.0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.5/maven-2.0.5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.6/maven-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.7/maven-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.8/maven-2.0.8.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0.9/maven-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.0/maven-2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.1.0/maven-2.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.0/maven-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/2.2.1/maven-2.2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.3/maven-3.0.3.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.4/maven-3.0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.0.5/maven-3.0.5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.0/maven-3.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.3.9/maven-3.3.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven/3.6.1/maven-3.6.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven/apache-maven_LICENSE.txt
/usr/share/package-licenses/mvn-maven/maven-core_checkstyle-license.txt
/usr/share/package-licenses/mvn-maven/maven-model_src_test_java_org_apache_maven_model_LicenseTest.java
