%define         sub_pkg_path %{nil}

Name:           ros-kinetic-std-msgs
Version:        0.5.11
Release:        0%{?dist}
Summary:        ROS std_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/std_msgs
Source0:        %{name}-%{version}.tar.gz
Source1:        cmake_manifest_parser
Source1001:     %{name}.manifest

BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-gencpp
BuildRequires:  ros-kinetic-geneus
BuildRequires:  ros-kinetic-genlisp
BuildRequires:  ros-kinetic-genpy
BuildRequires:  ros-kinetic-gennodejs
Requires:       ros-kinetic-message-runtime

%description
Standard ROS Messages including common message types representing primitive data
types and other basic message constructs, such as multiarrays. For common,
generic robot-specific message types, please see common_msgs.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__ros_setup}
%{__ros_build}

%install
%{__ros_setup}
%{__ros_install}

python %{SOURCE1} %{buildroot}

%files -f ros_install_manifest
%manifest %{name}.manifest
